
from django.shortcuts import render, redirect
from .forms import PortfolioForm


def portfolio_upload(request):

    formulario = PortfolioForm(request.POST, request.FILES)

    if request.method == "POST":
        portfolio = start(request.FILES["formulario_cliente"])
        return redirect("portfolio_display")



    return render(request, 'portfolio_upload.html', {"form": formulario})

def portfolio_display(request):

    portfolio = open("C:/Users/Felipe/PycharmProjects/AutomatizadorDePortifolio/webapp/output.txt", 'r')
    portfolio = portfolio.read()

    return render(request, 'portfolio_display.html', {"portfolio": portfolio})