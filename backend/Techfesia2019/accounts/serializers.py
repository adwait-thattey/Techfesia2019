from django.shortcuts import get_object_or_404
from rest_framework import serializers
import base.models as base_models
from registration.models import User
from . import path_resolvers

class ProfilePictureUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = base_models.ImageUploadModel
        fields = ('user', 'uploaded_image')


    def create(self, validated_data):

        img = base_models.ImageUploadModel(
                purpose="profile pic upload",
                user=validated_data['user'],
                upload_path=path_resolvers.resolve_user_profile_path(validated_data['user']),
                uploaded_image=validated_data['uploaded_image']
        )
        img.save()

        return img

    def update(self, instance, validated_data):
        raise NotImplementedError("update is not allowed on this serializer.\
         For purpose of logging, every file upload must happen in a new serializer")