from django.db.models import Count, Sum
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from components.models import Component
from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer


class SupplierCreateListView(generics.ListCreateAPIView):
    queryset=Supplier.objects.all()
    serializer_class=SupplierSerializer


class SupplierRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Supplier.objects.all()
    serializer_class=SupplierSerializer

    def delete(self, *args, **kwargs):
        instance=self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Supplier deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class Components:
    pass


class SupplierStatisticsView(APIView):
    queryset=Supplier.objects.all()

    def get(self, request):
        top_supplier= Component.objects.values('supplier__name').annotate(count=Count('id'),
                                                                          total_price=Sum('price_total')
                                                                          ).order_by('count')


        data={
            'top_supplier': top_supplier,

        }

        return Response(data)