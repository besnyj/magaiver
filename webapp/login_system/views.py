from django.shortcuts import render, redirect
import requests
from .assessor import Assessor
from .check import Check
import json



def login_user(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        credentials = Assessor(username, password)
        credentials = credentials.to_dict()
        print(credentials)

        isValidCredential = Check(**json.loads(requests.post('http://localhost:8080/', json=credentials).text))
        print(isValidCredential.value)

        if isValidCredential:
            redirect('portfolio')
        else:
            pass

    return render(request, 'authentication/login.html', {})

