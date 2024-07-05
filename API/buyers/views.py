from django.db.models import Count, Sum, Avg
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from API.buyers.models import Buyer
from API.buyers.serializers import BuyerSerializer
from API.sales.models import Sale
from setup.permissions import GlobalDefaultPermission


class BuyerCreateListView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Buyer.objects.all()
    serializer_class=BuyerSerializer


class BuyerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Buyer.objects.all()
    serializer_class=BuyerSerializer

    def delete(self, *args, **kwargs):
        instance=self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Buyer deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class BuyerStatisticsView(APIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Buyer.objects.all()

    def get(self, request):
        top_buyer=Sale.objects.values('buyer__name').annotate(buy=Count('id')).order_by('-buy')
        total_spending=Sale.objects.values('buyer__name').annotate(total_spending=Sum('total_value')).order_by(
            '-total_spending'),
        avg_spending=Sale.objects.values('buyer__name').annotate(avg_spending=Avg('total_value')).order_by(
            '-avg_spending')

        total_cash_outflow=Sale.objects.aggregate(total_outflow=Sum('total_value'))

        data={
            'top_buyer': top_buyer,
            'total_spending': total_spending,
            'avg_spending': avg_spending,
            'total_cash_outflow': total_cash_outflow

        }

        return Response(data)
