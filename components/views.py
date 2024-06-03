from rest_framework import generics
from components.models import Component
from components.serializers import ComponentSerializer


class ComponentCreateListView(generics.ListCreateAPIView):
    queryset=Component.objects.all()
    serializer_class=ComponentSerializer


class ComponentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Component.objects.all()
    serializer_class=ComponentSerializer
