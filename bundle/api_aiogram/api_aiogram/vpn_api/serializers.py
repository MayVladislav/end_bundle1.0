from rest_framework import serializers

from vpn_api.models import VpnModel1, VpnUserUseModel1


class VpnSerializer(serializers.ModelSerializer):
    class Meta:
        model = VpnModel1
        fields = '__all__'


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VpnUserUseModel1
        fields = '__all__'
