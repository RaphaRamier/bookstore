from django.db.models import Count, Sum, Avg
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from components.models import Component
from setup.permissions import GlobalDefaultPermission
from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer


class SupplierCreateListView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Supplier.objects.all()
    serializer_class=SupplierSerializer


class SupplierRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Supplier.objects.all()
    serializer_class=SupplierSerializer

    def delete(self, *args, **kwargs):
        instance=self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Supplier deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)





class SupplierStatisticsView(APIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Supplier.objects.all()

    def get(self, request):
        top_supplier= Component.objects.values('supplier__name').annotate(supply=Count('id')).order_by('-supply')
        total_spending=Component.objects.values('supplier__name').annotate(total_spending=Sum('price_total')).order_by(
            '-total_spending'),
        avg_spending=Component.objects.values('supplier__name').annotate(avg_spending=Avg('price_total')).order_by(
            '-avg_spending')

        total_cash_outflow = Component.objects.aggregate(total_outflow=Sum('price_total'))

        data={
            'top_supplier': top_supplier,
            'total_spending': total_spending,
            'avg_spending': avg_spending,
            'total_cash_outflow':total_cash_outflow

        }

        return Response(data)