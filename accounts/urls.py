from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
        path('register/', views.register, name='register'),
        path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='authentication/logout.html'), name='logout'),
        path('password-change/', auth_views.PasswordChangeView.as_view(
            template_name='authentication/change_password.html',
            success_url = '/password-change/done/'), name='password_change'),
        path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='authentication/password_change_done.html'), name='password_change_done'),
        path('password-reset/',
            auth_views.PasswordResetView.as_view(
            template_name='authentication/password_reset.html',
            email_template_name='authentication/password_reset_html_email.html',
            success_url = '/password-reset-done/'),name='password_reset'),
        path('password-reset-done/',
            auth_views.PasswordResetDoneView.as_view(
            template_name='authentication/password_reset_done.html'),
            name='password_reset_done'),
        path('password-reset-confirm/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(
            template_name='authentication/password_reset_confirm.html',
            success_url = '/password-reset-complete/'),
            name='password_reset_confirm',),
        path('password-reset-complete/',
            auth_views.PasswordResetCompleteView.as_view(
            template_name='authentication/password_reset_complete.html'),
            name='password_reset_complete'),
]
