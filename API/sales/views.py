from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from API.sales.models import Sale
from API.sales.serializers import SaleSerializer
from setup.permissions import GlobalDefaultPermission


class SaleCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Sale deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)