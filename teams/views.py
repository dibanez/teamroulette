from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from . import forms

def process_form(request, form_class):
    dictionary = {'name': 'Miguel'}
    if request.method == 'GET':
        form = form_class()
        dictionary['form'] = form
        return render(request,
                      'teams/index.html',
                      dictionary=dictionary)
    elif request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            if hasattr(form, 'save'):
                form.save()
            return redirect(reverse('home'))
        else:
            dictionary['form'] = form
            return render(request,
                          'teams/index.html',
                          dictionary=dictionary)

def team(request):
    form_class = forms.TeamForm
    return process_form(request, form_class)

def player(request):
    form_class = forms.PlayerModelForm
    return process_form(request, form_class)






