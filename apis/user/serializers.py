from rest_framework import serializers
from django.conf import settings
from user.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import PermissionDenied, NotFound, ValidationError


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    User Registration Serializer
    """

    name = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(
        max_length=100, required=True, label="Email Address")
    password = serializers.CharField(
        max_length=100, required=True, write_only=True, label="Password", style={'input_type': 'password'})

    class Meta(object):
        model = User
        fields = ['id', 'name', 'email', 'password']

    def validate_email(self, value):
        """
        Check email exist
        """
        value_lower = value.lower()
        if User.objects.filter(email=value_lower).exists():
            raise ValidationError({'email': "Email already exists."})
        return value

    def validate_password(self, value):
        """
        Check password length
        """
        if len(value) < getattr(settings, 'PASSWORD_MIN_LENGTH', 6):
            raise serializers.ValidationError(
                "Password should be at least %s characters long." % getattr(
                    settings, 'PASSWORD_MIN_LENGTH', 6)
            )
        return value

    def create(self, validated_data):
        """
        create user instance
        """
        email = validated_data['email'].lower()
        name = validated_data['name']

        user = User.objects.create(
            name=name,
            email=email,
            is_active=True
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user_id=user.id)
        return user



class UserLoginSerializer(serializers.ModelSerializer):
    """
    User Login Serializer
    """

    name = serializers.CharField(
        max_length=100, required=False, allow_blank=True, allow_null=True, label="Name")
    email = serializers.EmailField(
        max_length=100, required=True, label="Email Address")
    password = serializers.CharField(
        max_length=100, required=True, write_only=True, style={'input_type': 'password'})

    device_id = serializers.CharField(required=True, max_length=250, write_only=True, )

    token = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    club_member = serializers.ReadOnlyField()
    joined_clubs = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ['id', 'name', 'email', 'profile_image', 'password', 'token', 'club_member', 'joined_clubs',
                  'device_id']

    def validate(self, data):
        """
        Handle validation
        """
        email = data.get('email', None).lower()
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        if not user:
            raise NotFound("Invalid credential.try again")
        if user:
            if user.is_active:
                if user.all_groups.filter(name='user'):
                    return {
                        'id': user.id,
                        'name': user.name,
                        'email': user.email,
                        'profile_image': user.profile_image,
                        'token': Token.objects.get(user=user.id).key,
                    }
                else:
                    raise PermissionDenied("You do not have permission to perform this action.")
            else:
                raise NotFound("Your account has been deactivated.")
