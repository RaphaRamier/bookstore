import json
from datetime import datetime
from decimal import Decimal
import requests
from django.core.paginator import Paginator
from django.db.models import Sum, Avg
from django.db.models.functions import TruncMonth
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from requests.auth import HTTPBasicAuth

from API.books.models import Book
from API.cashflow.models import CashInFlow, CashOutFlow
from API.genres.views import GenreStashView
from API.publication.models import Publication
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
    genre_stash_view=GenreStashView()
    sale_trend_view=SaleMonthlyTrendView()
    response=sale_trend_view.get(request)
    genre_stash_response=genre_stash_view.get(request)

    data=[]
    last_genre_data={}

    if 'genres_trend' in response.data:
        genres_trend=response.data['genres_trend']

        for genre_data in genres_trend:
            genre=genre_data.get('genre')
            month=genre_data.get('month')
            total_quantity=genre_data.get('total_quantity')
            total_value=genre_data.get('total_value')
            revenue=genre_data.get('revenue')

            if genre and total_value is not None:
                last_genre_data[genre]={
                    'genre': genre,
                    'month': month,
                    'total_value': round(Decimal(total_value), 2),
                    'total_quantity': total_quantity,
                    'revenue': revenue
                }

        data=list(last_genre_data.values())
        genre_stash=genre_stash_response.data
        top_sales=data[:4]

        print(top_sales)

    return render(request, 'books/analytics.html', {'data': data, 'genre_stash': genre_stash, 'top_sales': top_sales})


@login_required
def balance(request):
    current_year=datetime.now().year
    last_year=current_year - 1
    sale_trend_view=SaleMonthlyTrendView()
    response=sale_trend_view.get(request)
    monthly_trends=response.data['monthly_trends'] if response.status_code == 200 else []

    dates=[entry['month'] for entry in monthly_trends]
    revenues=[float(entry['total_value']) for entry in monthly_trends]

    average_inflow_last_year= \
        CashInFlow.objects.filter(date__year=last_year, source__status='SUCCESSFUL').aggregate(average=Avg('amount'))[
            'average'] or Decimal('0.00')
    average_outflow_last_year=CashOutFlow.objects.filter(date__year=last_year).aggregate(average=Avg('amount'))[
                                  'average'] or Decimal('0.00')

    sales_goal=average_inflow_last_year * 12
    expense_limit=average_outflow_last_year * 12

    total_inflow=CashInFlow.objects.filter(source__status='SUCCESSFUL').aggregate(total=Sum('amount'))[
                     'total'] or Decimal('0.00')
    total_outflow=CashOutFlow.objects.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
    cash_flow=total_inflow - total_outflow

    sales_percentage=(total_inflow / sales_goal) * 100 if sales_goal > 0 else 0
    expense_percentage=(total_outflow / expense_limit) * 100 if expense_limit > 0 else 0

    books=Publication.objects.all()
    paginator=Paginator(books, 28)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    sales_done=Sale.objects.all().order_by('-sale_date')[:10]
    pending_purchases=Sale.objects.filter(status='PENDING').order_by('-sale_date')[:10]

    print(sales_percentage)

    context={
        'cashflow': {
            'total_inflow': total_inflow,
            'total_outflow': total_outflow,
            'cash_flow': cash_flow
        },
        'sales_percentage': sales_percentage,
        'expense_percentage': expense_percentage,
        'books_in_stock': page_obj,
        'sales_goal': sales_goal,
        'expense_limit': expense_limit,
        'sales_done': sales_done,
        'pending_purchases': pending_purchases,
        'revenues': json.dumps(revenues),
        'dates': json.dumps(dates),
    }
    return render(request, 'balance/balance.html', context)
