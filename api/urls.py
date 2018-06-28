from django.urls import path
from . import views

urlpatterns = [
    # /music/<album_id>
    path('<int:current_status>/', views.index, name='details'),
]