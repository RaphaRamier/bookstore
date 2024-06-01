from django.http import JsonResponse
from rest_framework import generics
from books.models import Book
from books.serializers import BookSerializer


class BookCreateListView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer


class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

    def delete(self, *args, **kwargs):
        instance=self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Book deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
