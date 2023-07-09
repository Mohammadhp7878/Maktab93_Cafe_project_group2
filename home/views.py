from django.shortcuts import render
from . import models
from .forms import ContactForm


def home(request):
    if request.method == "POST":
        print("method post deliverd....")
        form = ContactForm(request.POST)
        print(*request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            print(name, '-->', email, '-->', number)
        else:
            print('form not valid...')
    else:
        form = ContactForm()
    about_us = models.AboutUs.objects.order_by('-id').first()
    return render(request, 'base.html', {'about_us': about_us})
