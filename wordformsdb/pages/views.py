from django.shortcuts import render

from .models import Entry


def main(request):
    if request.user.is_staff:
        is_admin = True
    else:
        is_admin = False
    return render(request, 'pages/main.html', {'is_admin': is_admin})

def table(request):
    entries = Entry.objects.all()
    if request.user.is_staff:
        is_admin = True
    else:
        is_admin = False
    return render(request, 'pages/table.html', {'entries': entries, 'is_admin': is_admin})
