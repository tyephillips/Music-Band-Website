from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'horizons'
urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('member-area/', views.member_area, name='member_area'),
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='horizons/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
]
