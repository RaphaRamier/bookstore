from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
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
