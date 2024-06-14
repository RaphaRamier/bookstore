from django.shortcuts import render


# Create your views here.
def test_home(request):
    return render(request, 'cashflow/cashflow.html')
