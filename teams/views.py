from django.shortcuts import render

from . import forms


def main(request):
    form = forms.TeamForm()
    dictionary = {
        'name': 'David',
        'form': form,
    }
    return render(request,
                  'teams/index.html',
                  dictionary=dictionary)
