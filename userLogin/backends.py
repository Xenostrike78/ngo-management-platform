from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.db import connection

User = get_user_model()

class EmailOrMobileBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Try to find a user by email or mobile number
        try:
            user = User.objects.get(email=username)  # Assuming username is email
        except User.DoesNotExist:
            try:
                user = User.objects.get(mobile=username)  # If using mobile number
            except User.DoesNotExist:
                return None

        if user and check_password(password, user.password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
