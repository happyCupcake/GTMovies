from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signup, name="accounts.signup"),
    path('login/', views.login, name="accounts.login"),
    path('logout/', views.logout, name="accounts.logout"),
    path('orders/', views.orders, name="accounts.orders"),
    path('password_reset/', views.password_reset, name='accounts.password_reset'),
    path('password_reset_done/', views.password_reset_done, name='accounts.password_reset_done'),
]