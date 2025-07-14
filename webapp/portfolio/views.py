from django.shortcuts import render
from .forms import PortfolioForm
from .backend.start import start

def portfolio_upload(request):
    if request.method == "POST":

        formulario = PortfolioForm(request.POST, request.FILES)
        if formulario.is_valid():
            start(formulario)


    return render(request, 'portfolio_upload.html', {})