from decimal import Decimal
import requests
from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from requests.auth import HTTPBasicAuth
from API.cashflow.models import CashInFlow, CashOutFlow
from API.genres.views import GenreStashView
from API.sales.models import Sale
from API.sales.views import SaleMonthlyTrendView
from API.services.models import Service
from Client import user


@login_required
def home(request):
    sale_trend_view=SaleMonthlyTrendView()
    response=sale_trend_view.get(request)

    sales=Sale.objects.all()
    sales_list=sales[:20]
    sales_done=sales[:10]
    total_inflow=round(CashInFlow.objects.filter(source__status='SUCCESSFUL').aggregate(total=Sum('amount'))['total'],
                       2) or 0
    total_outflow=round(CashOutFlow.objects.aggregate(total=Sum('amount'))['total'], 2)

    percentage_difference=None
    if 'monthly_trends' in response.data:
        monthly_trends=response.data['monthly_trends']
        if monthly_trends:
            last_month_data=monthly_trends[0]
            percentage_difference=round(last_month_data.get('percentage_difference'), 2)

    try:
        cash_flow=total_inflow - total_outflow
    except:
        cash_flow=0

    services=CashOutFlow.objects.all()
    services_list=services
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

    print(percentage_difference)

    return render(request, 'cashflow/cashflow.html',
                  {'sales_list': sales_list,
                   'sales_done': sales_done,
                   'top_sales': top_sales,
                   'cashflow': cashflow,
                   'services_list': services_list,
                   'percentage_difference': percentage_difference,
                   })


def analytics(request):
    genre_stash_view = GenreStashView()
    sale_trend_view = SaleMonthlyTrendView()
    response = sale_trend_view.get(request)
    genre_stash_response=genre_stash_view.get(request)

    data = []
    last_genre_data = {}

    if 'genres_trend' in response.data:
        genres_trend = response.data['genres_trend']

        for genre_data in genres_trend:
            genre = genre_data.get('genre')
            month = genre_data.get('month')
            total_quantity = genre_data.get('total_quantity')
            total_value = genre_data.get('total_value')
            revenue = genre_data.get('revenue')

            if genre and total_value is not None:
                last_genre_data[genre] = {
                    'genre': genre,
                    'month': month,
                    'total_value': round(Decimal(total_value), 2),
                    'total_quantity': total_quantity,
                    'revenue':revenue
                }

        data = list(last_genre_data.values())
        genre_stash=genre_stash_response.data
        top_sales=data[:4]

        print(top_sales)

    return render(request, 'books/analytics.html', {'data': data, 'genre_stash':genre_stash, 'top_sales':top_sales})
