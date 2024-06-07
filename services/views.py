from services.models import Service
from services.serializers import ServiceSerializer
from django.db.models import Count, Sum, Avg
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from setup.permissions import GlobalDefaultPermission


class ServiceCreatListView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer


class ServiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer

    def delete(self, *args, **kwargs):
        instance=self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Service deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
