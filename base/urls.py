from django.urls import path
from . import views  # Import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addtocart/<int:pk>/', views.addtocart, name='addtocart'),
    path('cart/', views.cart, name='cart'),
    path('remove/<int:pk>/', views.remove, name='remove'),

    # Correctly reference add and sub from views
    path('add/<int:pk>/', views.add, name='add'),
    path('sub/<int:pk>/', views.sub, name='sub'),
]
