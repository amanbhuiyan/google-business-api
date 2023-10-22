from django.urls import path
from . import views

urlpatterns = [
    path('businesses/<str:city_name>/', views.get_businesses_without_reviews, name='businesses'),
    # path('businesses/<str:city_name>/1', views.get_businesses_based_on_ratings, name='businesses'),
    path('businesses/<str:city_name>/<int:ratinginput>', views.get_businesses_based_on_ratings, name='businesses'),
]
