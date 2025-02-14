from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm
urlpatterns = [
    path('signup', views.signup, name="accounts.signup"),
    path('login/', views.login, name="accounts.login"),
    path('logout/', views.logout, name="accounts.logout"),
    path('orders/', views.orders, name="accounts.orders"),

    # Password Reset Views

    # Password Reset View (where the user enters their email)
    path('password_reset/', auth_views.PasswordResetView.as_view(
        form_class=CustomPasswordResetForm,
        template_name='accounts/password_reset_form.html',
        success_url='/accounts/password_reset/done/'
    ), name="accounts.password_reset"),

    # Password Reset Done (confirmation page after email is sent)
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name="accounts.password_reset_done"),

    # Password Reset Confirmation (where the user enters a new password)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'
    ), name="password_reset_confirm"),

    # Password Reset Complete (after the user has reset their password)
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name="password_reset_complete")

]