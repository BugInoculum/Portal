from rest_framework import serializers
from gig.models import *


class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:

        model = CustomUser
        fields = "__all__"



class ProjectSerializer(serializers.ModelSerializer):

    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Project

        fields = ('')