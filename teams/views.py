from django.shortcuts import render, redirect

from . import forms


def main(request):
    if request.method == 'GET':
        form = forms.TeamForm()
        dictionary = {
                     'name': 'David',
                     'form': form,
                     }
        return render(request,
                      'teams/index.html',
                      dictionary=dictionary)
    elif request.method == 'POST':
        form = forms.TeamForm(data=request.POST)
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