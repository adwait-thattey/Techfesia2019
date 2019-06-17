from firebase_admin import auth
from rest_framework import serializers

from registration.models import User, FirebaseUser


class FirebaseUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    uid = serializers.CharField(max_length=100)

    def validate(self, data):
        # print("Hello")
        user = User.objects.filter(username=data['username'])
        if not user.exists():
            raise serializers.ValidationError("This user does not exist!")

        user = user[0]

        data['user'] = user

        return data

    def perform_firebase_auth(self, validated_data):
        user = validated_data['user']
        try:
            firebase_user = auth.get_user(validated_data['uid'])
        except auth.AuthError:
            print(validated_data['uid'])
            raise serializers.ValidationError("Invalid uid or No user found with the given uid")

        except:
            raise serializers.ValidationError(
                "We were unable to verify the credentials from sources. Please try again Later! ")

        if firebase_user.email != user.email:
            raise serializers.ValidationError("uid mismatch!")

        if hasattr(user,'firebaseuser'):
            user.firebaseuser.uid = validated_data['uid']
        else:
            FirebaseUser.objects.create(user=user, uid=validated_data['uid'])

        try:
            user.firebaseuser.profile_pic_url = firebase_user.photo_url
        except:
            # No photo is attached!
            pass

        user.firebaseuser.save()

        return user.firebaseuser

    def create(self, validated_data):
        return self.perform_firebase_auth(validated_data)

    def update(self, instance, validated_data):
        return self.perform_firebase_auth(validated_data)


class FirebaseTokenObtainSerializer(serializers.Serializer):

    email_field = User.EMAIL_FIELD

    def __init__(self, *args, **kwargs):
        super(FirebaseTokenObtainSerializer, self).__init__(*args, **kwargs)

        self.fields[self.email_field] = serializers.CharField()
        self.fields['uid'] = serializers.CharField()
        self.user = None

    def validate(self, attrs):
        email = attrs['email']
        uid = attrs['uid']

        try:
            firebase_user = auth.get_user(uid)
            if firebase_user.email != email:
                print(firebase_user.email, email)
                raise serializers.ValidationError(
                    _('Invalid Credentials'),
                )
            self.user = User.objects.get(email=email)
        except serializers.ValidationError:
            raise serializers.ValidationError(
                _('No active account found with the given credentials'),
            )

        except User.DoesNotExist:
            raise serializers.ValidationError(
                _(
                    'Currently no account exists. First create an account with the given email. Then try to attach firebase')
            )
        return {}

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class FirebaseTokenObtainPairSerializer(FirebaseTokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super(FirebaseTokenObtainPairSerializer, self).validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = text_type(refresh)
        data['access'] = text_type(refresh.access_token)

        return data