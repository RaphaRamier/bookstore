from django.db.models import Sum, Avg
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from API.genres.models import Genre
from API.genres.serializers import GenreSerializer
from API.publication.models import Publication
from setup.permissions import GlobalDefaultPermission
from rest_framework.permissions import IsAuthenticated


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Genre deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class GenreStashView(APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Publication.objects.all()

    def get(self, request):
        genres_stock = self.queryset.values('book__genres__name').annotate(
            total_quantity=Sum('quantity'),
            total_price = Sum('price_total'),
            average_price=Avg('price_unit')
        )

        data = []

        for item in genres_stock:
            genre = item['book__genres__name']
            total_price = item['total_price']
            total_quantity = item['total_quantity']
            average_price = item['average_price']

            data.append({
                'genre': genre,
                'total_price':round(total_price, 2) if total_price else None,
                'total_quantity': total_quantity if total_quantity else None,
                'average_price': round(average_price, 2) if average_price else None
            })



        return Response(data)