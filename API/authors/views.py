from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from API.authors.models import Authors
from API.authors.serializers import AuthorSerializer
from setup.permissions import GlobalDefaultPermission


class AuthorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Author deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)