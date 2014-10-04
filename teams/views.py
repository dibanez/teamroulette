from django.shortcuts import render


def main(request):
    return render(request,
                  'teams/index.html',
                  dictionary={'name': 'David'})
