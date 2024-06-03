from django.db.models import Count
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authors.models import Authors
from books.models import Book
from books.serializers import BookSerializer
from genres.models import Genre
from setup.permissions import GlobalDefaultPermission


class BookCreateListView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Book.objects.all()
    serializer_class=BookSerializer


class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Book.objects.all()
    serializer_class=BookSerializer

    def delete(self, *args, **kwargs):
        instance=self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Book deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class BookStatisticsView(APIView):
    queryset=Book.objects.all()
    def get(self, request):

        genre_counts=self.queryset.values('genres__name').annotate(count=Count('id'))
        author_per_genre = self.queryset.values('genres__name').annotate(count=Count('author'))
        books_per_author = self.queryset.values('author__name').annotate(count=Count('id'))



        data={
            'genre_counts': genre_counts,
            'author_per_genre': author_per_genre,
            'books_per_author': books_per_author,
        }

        return Response(data)
