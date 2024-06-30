import json
from datetime import datetime
from decimal import Decimal
import requests
from django.core.paginator import Paginator
from django.db.models import Sum, Avg
from django.db.models.functions import TruncMonth
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from requests.auth import HTTPBasicAuth

from API.authors.models import Authors
from API.books.models import Book
from API.cashflow.models import CashInFlow, CashOutFlow
from API.genres.models import Genre
from API.genres.views import GenreStashView
from API.publication.models import Publication
from API.sales.models import Sale
from API.sales.views import SaleMonthlyTrendView
from API.services.models import Service
from Client import user
from .forms import BookForm, AuthorForm, GenreForm, BookAssemblyForm, PublicationForm


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


def add_book(request):
    book_form=BookForm()
    author_form=AuthorForm()
    genre_form=GenreForm()
    assembly_form=BookAssemblyForm()
    publication_form=PublicationForm()

    if request.method == 'POST':
        item_type=request.POST.get('item-type')
        if item_type == 'book':
            form=BookForm(request.POST)
        elif item_type == 'author':
            form=AuthorForm(request.POST)
        elif item_type == 'genre':
            form=GenreForm(request.POST)
        elif item_type == 'assembly':
            form=BookAssemblyForm(request.POST)
        elif item_type == 'publication':
            form=PublicationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('success_url')

    context={
        'book_form': book_form,
        'author_form': author_form,
        'genre_form': genre_form,
        'assembly_form': assembly_form,
        'publication_form': publication_form
    }
    return render(request, 'forms/book_forms.html', context)


@login_required
def book_shelf(request):
    books=Publication.objects.all()
    paginator=Paginator(books, 12)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request, 'book_shelf/shelf.html', {'books': books, 'total_books': page_obj})


@login_required
def book_detail(request, id):
    book=get_object_or_404(Book, id=id)
    return render(request, 'book_shelf/book_detail.html', {'book': book})


@login_required
def edit_book(request, book_id):
    book=get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form=BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', id=book.id)
    else:
        form=BookForm(instance=book)
    return render(request, 'forms/edit_book.html', {'form': form, 'book': book})


@login_required()
def authors_list(request):
    authors=Authors.objects.all()
    paginator=Paginator(authors, 12)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request, 'authors/authors_list.html', {'authors': authors, 'authors_list': page_obj})

@login_required
def author_detail(request, author_id):
    author = get_object_or_404(Authors, id=author_id)
    books = Book.objects.filter(author=author)
    context = {
        'author': author,
        'books': books,
    }
    return render(request, 'authors/author_detail.html', context)


@login_required
def books_by_genre(request):
    genres=Genre.objects.all()
    selected_genre=request.GET.get('genre')

    if selected_genre and selected_genre != 'all':
        books=Publication.objects.filter(book__genres__id=selected_genre)
    else:
        books=Publication.objects.all()

    paginator=Paginator(books, 12)  # Mostra 12 livros por página
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    context={
        'genres': genres,
        'books': page_obj,
        'total_books': books.count(),
        'selected_genre': selected_genre
    }
    return render(request, 'genre/books_by_genre.html', context)
