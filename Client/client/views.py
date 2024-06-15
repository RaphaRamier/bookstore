from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from API.sales.models import Sale


@login_required
def home(request):
    sales_list=Sale.objects.all()[:20]
    paginator=Paginator(sales_list, 20)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request, 'cashflow/cashflow.html', {'page_obj':sales_list})
