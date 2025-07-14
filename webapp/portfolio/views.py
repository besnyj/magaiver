
from django.shortcuts import render, redirect
from .forms import PortfolioForm
from .backend.start import start

def portfolio_upload(request):

    formulario = PortfolioForm(request.POST, request.FILES)

    if request.method == "POST":

        start(request.FILES["formulario_cliente"])


    return render(request, 'portfolio_upload.html', {"form": formulario})