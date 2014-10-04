from django.shortcuts import render, redirect

from . import forms


def process_form(request, form_class):
    if request.method == 'GET':
        form = form_class()
        dictionary = {
                     'name': 'David',
                     'form': form,
                     }
        return render(request,
                      'teams/index.html',
                      dictionary=dictionary)
    elif request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            return redirect('/')
        else:
            dictionary = {
                        'name': 'David',
                        'form': form,
                        }
            return render(request,
                          'teams/index.html',
                          dictionary=dictionary)

def main(request):
    form_class = forms.TeamForm
    return process_form(request, form_class)
