from django.shortcuts import render


# Create your views here.
def index(request, current_status):
    return render(request, 'index.html', {'current_status': current_status})