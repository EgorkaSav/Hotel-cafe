from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from .views import user_login

urlpatterns = [
    path('', views.home, name='home'),    
    path('home', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('rooms/', views.rooms, name='rooms'),
    path('book/', views.book_room, name='book_room'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'), 
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('login/', user_login, name='login'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('sklad/', views.sklad_view, name='sklad'),
]

