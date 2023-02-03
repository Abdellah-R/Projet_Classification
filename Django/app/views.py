from django.shortcuts import render
from .forms import ApiForm
import requests
import json

# Create your views here.
def home(request):
    # header = {'accept': 'application/json',
    # 'Content-Type': 'application/json'}

    form = ApiForm(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            data = json.dumps(form.cleaned_data)
            reponse = requests.post('https://projet-classification-sba.onrender.com/predict', data=data)
            info = json.loads(reponse.text)
            print(info)
            return render(request, 'app/home.html', context={'form' : form, 'info' : info} )

    context = {'form' : form}
    return render(request, 'app/home.html', context=context )
