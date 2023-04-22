from rest_framework import serializers
from users.models import User, Profile
from photo_upload.models import Target

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data.pop('user')
        profile = Profile.objects.create(**validated_data)
        User.objects.create(profile=profile, **user)
        return profile

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'