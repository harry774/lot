from django.shortcuts import render
from .models import Status
from django.http import HttpResponse


# Create your views here.
def index(request):
    st = Status.objects.get(pk=1)
    return render(request, 'index.html', {'current_status': st.status})


def store(request, current_status):
    newst = Status.objects.get(pk=1)
    newst.status = current_status
    newst.save()
    return HttpResponse('done')
