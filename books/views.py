from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from books.models import Book
from books.serializers import BookSerializer
from setup.permissions import GlobalDefaultPermission


class BookCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset=Book.objects.all()
    serializer_class=BookSerializer


class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset=Book.objects.all()
    serializer_class=BookSerializer

    def delete(self, *args, **kwargs):
        instance=self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Book deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
