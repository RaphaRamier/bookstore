import requests
from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from requests.auth import HTTPBasicAuth

from API.cashflow.models import CashInFlow, CashOutFlow
from API.sales.models import Sale
from API.services.models import Service
from Client import user


@login_required
def home(request):
    sales=Sale.objects.all()
    sales_list=sales[:20]
    sales_done=sales[:10]
    total_inflow=CashInFlow.objects.aggregate(total=Sum('amount'))['total']
    total_outflow=CashOutFlow.objects.aggregate(total=Sum('amount'))['total']

    try:
        cash_flow=total_inflow - total_outflow
    except:
        cash_flow= 0


    services=Service.objects.all()
    services_list=services[:10]
    top_sales=sales.order_by('-quantity')[:3]

    try:
        cashflow={
            'total_inflow': total_inflow,
            'total_outflow': total_outflow,
            'cash_flow': cash_flow

        }
    except:
        cashflow={
            'total_inflow': 0,
            'total_outflow': 0,
            'cash_flow': 0
        }

    return render(request, 'cashflow/cashflow.html',
                  {'sales_list': sales_list,
                   'sales_done': sales_done,
                   'top_sales': top_sales,
                   'cashflow': cashflow,
                   'services_list': services_list
                   })
