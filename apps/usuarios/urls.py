from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Registrar
    path("registrar-pessoa/", registrar_pessoa, name="registrar_pessoa"),
    
    # Listar
    path("listar-pessoas/", listar_pessoas, name="listar_pessoas"),

    # Perfil
    path("perfil-usuario/", perfil_usuario, name="perfil_usuario"),

    #SIGN UP
    path('signup/', SignUpView.as_view(), name='signup'),
    
    #LOGIN
    path("login/", auth_views.LoginView.as_view(template_name="usuarios/login/login.html"), name="login"),
    
    #LOGOUT
    path("logout/", auth_views.LogoutView.as_view(template_name="usuarios/logout/logout.html"), name="logout"),
    
    #RESET PASSWORD
    path('reset-password/sent/', auth_views.PasswordResetDoneView.as_view(template_name="usuarios/reset_password/reset-password-done.html"), name="password_reset_done"),
    path('reset-password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="usuarios/reset_password/reset-password-confirm.html"), name="password_reset_confirm"),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name="usuarios/reset_password/reset-password-complete.html"), name="password_reset_complete"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="usuarios/reset_password/reset-password.html"), name="reset_password"),
    
    #VALIDATE
    url('validate/email/', validate_email, name='validate_email'),
    url('validate/user/', validate_user, name='validate_user'),
    url('validate/email-registered/', validate_email_registered, name='validate_email_registered'),
]
