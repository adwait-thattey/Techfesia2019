# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import generics
from registration.models import User
from registration.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from registration.permissions import IsStaffUserOrPost, IsStaffUser, IsStaffUserOrAuthenticated
from rest_framework_simplejwt import tokens

# Create your views here.


# class UsersView(generics.ListAPIView):
#     permission_classes = (IsStaffUser,)
#     # limit = int(super().request.query_params['limit'])
#     queryset = models.User.objects.filter(is_staff=False)
#     serializer_class = UserSerializer


class UsersViewPost(APIView):
    permission_classes = (IsStaffUserOrPost,)

    def get(self, request, format=None):
        print(request.query_params)
        limit, page = 3, 1
        if request.query_params.get('limit') is not None:
            limit = int(request.query_params.get('limit'))
        if request.query_params.get('page') is not None:
            page = int(request.query_params.get('page'))
        users = User.objects.order_by('username')
        if users.count()//limit + 1 < page:
            data = {"message": "This page does not exist", "pageSize": limit, "noOfPages": page}
        else:
            users = users[(page-1)*limit, page*limit]
            serializer = UserSerializer(users, many=True)
            data = {'users': serializer.data, "currentPage": page, "noOfPages": users.count()//limit+1}

        return Response(data)

    def post(self, request, format=None):
        print(request.data)
        data = UserSerializer(data=request.data)
        print(data)
        print(data.is_valid())
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            errors = []
            if request.POST.get('username') is None:
                errors.append(('username', 'Please provide a username'))
            elif User.objects.filter(username=request.POST.get('username')).count() > 0:
                errors.append(('username', 'This username already exists'))
            elif request.POST['username'] == '' or request.POST['username'] is None:
                errors.append(('username', 'missing required field'))
            return Response(JSONRenderer().render({'errors': dict(errors)}))


class UserDetail(APIView):
    permission_classes = (IsStaffUserOrAuthenticated,)

    def get(self, request, username, format=None):
        user = User.objects.get(username=username)
        data = UserSerializer(user).data
        return Response(data)

    def put(self, request, username, format=None):
        user = User.objects.get(username=username)
        data = UserSerializer(user, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            # To be Done Later
            return Response(JSONRenderer().render({'error': 'unable to update'}))

    def delete(self, request, username, ):
        user = User.objects.get(username=username)
        if user is not None:
            user.delete()
            return Response(JSONRenderer().render({'success': 'user deleted'}))
        else:
            return Response(JSONRenderer().render({'error': 'user not found'}))


class UserState(APIView):
    permission_classes = (IsStaffUser,)

    def get(self, request, username, format=None):
        user = User.objects.get(username=username)
        if not user.is_active:
            state = "disabled"
        elif user.is_superuser:
            state = "superuser"
        elif user.is_staff:
            state = "staff"
        else:
            state = "normal"
        return Response(JSONRenderer().render({'state': state}))


class StaffView(generics.ListAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer


class ProfilePictureUpload(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, username, format=None):
        # To be Done Later
        return JSONRenderer().render({'message': 'Profile Picture update'})


class DisableUser(APIView):
    permission_classes = (IsStaffUser,)

    def put(self, request, username, format=None):
        user = User.objects.get(username=username)
        if user is not None:
            user.is_active = False
            user.save()
            return Response(JSONRenderer().render({'success': 'user disabled'}))
        else:
            return Response(JSONRenderer().render({'error': 'user not found'}))


class UserPasswordSetReset(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, username, format=None):
        user = request.user
        if user.username == username:
            user.set_password(request.POST['password'])
            user.save()
            return Response(JSONRenderer().render({"message": "new password created"}))
        else:
            return Response(JSONRenderer().render({"message": "password creation unsuccessful"}))

    def put(self, request, username, format=None):
        user = request.user
        old_password, new_password = request.POST['oldPassword'], request.POST['newPassword']
        if user.username == username and user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(JSONRenderer().render({"message": "new password created"}))
        else:
            return Response(JSONRenderer().render({"message": "password update unsuccessful"}))

        # To add Checking reset Token
    def patch(self, request, username, format=None):
        user = User.objects.get(username=username)
        # if tokens.RefreshToken.verify(request.POST['resetToken']):
        if user.username == username:
            user.set_password(request.POST['newPassword'])
            user.save()
            return Response(JSONRenderer().render({"message": "password reset successful"}))
        else:
            return Response(JSONRenderer().render({"message": "password reset unsuccessful"}))


