from django.urls import path
from . import views
from .views import ChangeTargetImage

urlpatterns = [
    path('users/', views.get_user_data),
    path('add-user/', views.add_user),
    path('profiles/', views.get_profile_data),
    # path('add-profile/', views.add_profile),
    path('targets/', views.get_target_data),
    path('add-target/', views.add_target),
    path('target/<pk>/', views.get_target_num),
    path('change-target-photo/<pk>/', ChangeTargetImage.as_view()),
]