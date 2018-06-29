from django.urls import path
from . import views

urlpatterns = [
    # /music/<album_id>
    path('', views.index),
    path('<int:current_status>/', views.store),
]