from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
    path('contact/', views.contact_view, name='contact'),
]
