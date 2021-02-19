from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id_no',
            'phone_no',
            'region',
            'age',
            'gender',
        )

class CharitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charities
        fields = '__all__'

class DonationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationType
        fields = '__all__'


class DonationsSerializer(serializers.ModelSerializer):
    charity = CharitiesSerializer(read_only=True)
    donated_type = DonationTypeSerializer(read_only=True)

    class Meta:
        model = Donations
        fields = (
            'charity',
            'donated_type',
            'status',
            'date_created',
        )

