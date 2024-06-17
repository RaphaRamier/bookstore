from django.db.models import Sum
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from setup.permissions import GlobalDefaultPermission
from .models import CashInFlow, CashOutFlow
from rest_framework import generics
from .serializers import CashInFlowSerializer, CashOutFlowSerializer


class CashInFlowCreateListView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=CashInFlow.objects.all()
    serializer_class=CashInFlowSerializer


class CashInFlowRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=CashInFlow.objects.all()
    serializer_class=CashInFlowSerializer


class CashOutFlowCreateListView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=CashOutFlow.objects.all()
    serializer_class=CashOutFlowSerializer


class CashOutFlowRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=CashOutFlow.objects.all()
    serializer_class=CashOutFlowSerializer


class CashFlowView(APIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)

    def get(self, request):
        total_inflow=CashInFlow.objects.aggregate(total=Sum('amount'))['total']
        total_outflow=CashOutFlow.objects.aggregate(total=Sum('amount'))['total']
        cash_flow=total_inflow - total_outflow

        data={
            'total_inflow': total_inflow,
            'total_outflow': total_outflow,
            'cash_flow': cash_flow

        }
        return Response(data)
