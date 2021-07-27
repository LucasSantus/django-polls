from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # PESSOA
    path("pessoa/registrar/", registrar_pessoa, name="registrar_pessoa"),
    path("pessoa/listar/", listar_pessoas, name="listar_pessoas"),

    # Perfil
    path("usuario/perfil/", perfil_usuario, name="perfil_usuario"),

    #SIGN UP
    path('signup/', SignUpView.as_view(), name='signup'),
    
    #LOGIN
    path("login/", auth_views.LoginView.as_view(template_name="usuarios/login/login.html"), name="login"),
    
    #LOGOUT
    path("logout/", auth_views.LogoutView.as_view(template_name="usuarios/logout/logout.html"), name="logout"),
    
    #RESET PASSWORD
    path('password/reset/sent/', auth_views.PasswordResetDoneView.as_view(template_name="usuarios/reset_password/reset-password-done.html"), name="password_reset_done"),
    path('password/reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="usuarios/reset_password/reset-password-confirm.html"), name="password_reset_confirm"),
    path('password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name="usuarios/reset_password/reset-password-complete.html"), name="password_reset_complete"),
    path('password/reset/', auth_views.PasswordResetView.as_view(template_name="usuarios/reset_password/reset-password.html"), name="reset_password"),
]
