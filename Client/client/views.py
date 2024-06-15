import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    sales_response=requests.get('http://127.0.0.1:8000/API/sales/')
    if sales_response.status_code == 200:
        sales_list=sales_response.json()[:20]
    else:
        sales_list=[]

    cashflow_response=requests.get('http://127.0.0.1:8000/API/cashflow/')

    if cashflow_response.status_code == 200:
        cashflow=cashflow_response.json()
    else:
        cashflow={
            'total_inflow': 0,
            'total_outflow': 0,
            'cash_flow': 0,
        }

    return render(request, 'cashflow/cashflow.html', {'sales_list': sales_list, 'cashflow': cashflow})
