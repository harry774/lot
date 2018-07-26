from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # /music/<album_id>
    path('', views.index),
    path('<int:current_status>/', views.store),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
