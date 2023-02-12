from django.urls import path
from . import views
from .views import MenuItemsView, SingleItemMenuView

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleItemMenuView.as_view()),
]