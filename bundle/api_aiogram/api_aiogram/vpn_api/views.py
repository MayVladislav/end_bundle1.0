from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from vpn_api.models import VpnModel1, VpnUserUseModel1
from vpn_api.serializers import VpnSerializer, UserDataSerializer


class VpnApiView(generics.ListAPIView):
    queryset = VpnModel1.objects.all()
    serializer_class = VpnSerializer


class GetLastItemApiView(generics.ListAPIView):
    queryset = VpnModel1.objects.order_by('-id')[:1]
    serializer_class = VpnSerializer
    # lookup_field = ('pk')


class RemoveLastItemApiView(APIView):
    def delete(self, request, *args, **kwargs):
        try:
            last_item = VpnModel1.objects.latest('id')
            serializer = VpnSerializer(last_item)
            last_item.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except VpnModel1.DoesNotExist:
            return Response("No items to delete", status=status.HTTP_404_NOT_FOUND)


class GetUserUseInfo(generics.CreateAPIView):
    queryset = VpnUserUseModel1.objects.all()
    serializer_class = UserDataSerializer
