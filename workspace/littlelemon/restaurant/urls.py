from django.urls import path
from . import views
from .views import MenuItemsView, SingleItemMenuView, BookingView, SingleBookingItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleItemMenuView.as_view()),
    path('booking/', views.BookingView.as_view()),
    path('booking/<int:pk>', views.SingleBookingItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]