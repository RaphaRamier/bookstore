from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

from assembly.models import BookAssembly
from rest_framework import generics
from assembly.serializers import BookAssemblySerializer
from setup.permissions import GlobalDefaultPermission


class BookAssemblyCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = BookAssembly.objects.all()
    serializer_class = BookAssemblySerializer


class BookAssemblyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = BookAssembly.objects.all()
    serializer_class = BookAssemblySerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Assembly deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)