from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='photo-upload-home'),
    # path('edit/', views.change_photos, name='photo-upload-edit'),
]