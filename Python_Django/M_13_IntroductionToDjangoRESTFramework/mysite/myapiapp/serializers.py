from django.contrib.auth.models import Group
from rest_framework import serializers


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "pk", "name"