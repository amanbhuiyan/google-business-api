from django.urls import path
from . import views

urlpatterns = [
    path('businesses/<str:city_name>/', views.get_businesses_without_reviews, name='businesses'),
]
