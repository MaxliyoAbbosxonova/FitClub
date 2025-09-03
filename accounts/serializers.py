from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from accounts.models import Profile

User=get_user_model()

class UserProfileSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15, required=True)
    first_name = serializers.CharField(max_length=30, allow_blank=True, required=False, validators=[])
    last_name = serializers.CharField(max_length=30, allow_blank=True, required=False)
    email = serializers.EmailField(allow_blank=True, required=False)
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    username=serializers.CharField(max_length=30,allow_null=True)
    birth = serializers.DateField(required=False)


    def validate(self, attrs):
        password = attrs.get('password')
        if password:
            password_confirm = attrs.get('password_confirm')
            if not password_confirm:
                raise serializers.ValidationError({"password_confirm": "Password confirm ni tasdiqlang."})

            if attrs['password'] != attrs['password_confirm']:
                raise serializers.ValidationError('Password va Password confirm bir xil emas.')
        return attrs

    def create(self, validated_data):
        password=validated_data.pop('password',None)
        validated_data.pop('password_confirm')
        birth=validated_data.pop('birth')
        with transaction.atomic():
            user=User.objects.create(**validated_data)
            user.set_password(password)
            user.save()
            Profile.objects.create(user=user,birth=birth)
        return user

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        profile = instance.profile

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        if password:
            instance.set_password(validated_data['password'])
        instance.save()

        profile.birth = validated_data.get('birth', profile.birth)
        profile.save()

        return instance

    def to_representation(self, instance):
        profile = instance.profile if hasattr(instance, 'profile') else None
        birth = profile.birth if profile else None

        return {
            "id": instance.id,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "email": instance.email,
            "profile": {
                "id": instance.profile.id,
                "birth": birth
            }
        }
