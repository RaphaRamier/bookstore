from django.http import JsonResponse

from assembly.models import BookAssembly
from rest_framework import generics
from assembly.serializers import BookAssemblySerializer


class BookAssemblyCreateListView(generics.ListCreateAPIView):
    queryset = BookAssembly.objects.all()
    serializer_class = BookAssemblySerializer


class BookAssemblyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookAssembly.objects.all()
    serializer_class = BookAssemblySerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Assembly deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)