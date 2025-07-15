from django.shortcuts import render, redirect
import requests
from .models import Assessor
import json



def login_user(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        credentials = Assessor(username, password)
        credentials = credentials.to_dict()

        r = requests.post('http://localhost:8080/', json=credentials)
        print(r.text)

        # if user is not None:
        #     login(request, user)
        #     return redirect('portfolio')
        # else:
        #     messages.success(request, ("Error"))

    return render(request, 'authentication/login.html', {})

