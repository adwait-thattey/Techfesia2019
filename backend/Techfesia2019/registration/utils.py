from firebase_admin import auth
from rest_framework import serializers


class FirebaseUtils:

    @staticmethod
    def check_firebase_credentials(email, uid):
        """
        Checks whether the email matches with the email of firebase user.
        If true, returns firebase user object. Else raises appropriate exceptions
        """
        try:
            user_from_firebase = auth.get_user(uid)
            if user_from_firebase.email != email:
                # incorrect email provided
                raise serializers.ValidationError("uid mismatch")

            return user_from_firebase
        except auth.AuthError:
            # UID does not exist
            raise serializers.ValidationError("Invalid uid or No user found with the given uid")
        except:
            print("ERROR: UNABLE TO CONNECT TO FIREBASE")
            raise serializers.ValidationError("Unable to connect to firebase")