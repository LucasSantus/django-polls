from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views import *
from users.validate import *

urlpatterns = [
    path('accounts/', include([
        #SIGN UP
        path('signup/', signup.as_view(), name='signup'),

        #LOGIN
        path('login/', auth_views.LoginView.as_view(template_name="users/login/login.html"), name="login"),

        #LOGOUT
        path("logout/", auth_views.LogoutView.as_view(template_name="users/logout/logout.html"), name="logout"),

        #RESET PASSWORD
        path('password/reset/', include([
            path('sent/', auth_views.PasswordResetDoneView.as_view(template_name="users/reset_password/reset-password-done.html"), name="password_reset_done"),
            path('<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="users/reset_password/reset-password-confirm.html"), name="password_reset_confirm"),
            path('complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/reset_password/reset-password-complete.html"), name="password_reset_complete"),
            path('', auth_views.PasswordResetView.as_view(template_name="users/reset_password/reset-password.html"), name="reset_password"),
        ]))
    ])),

    # VALIDATE
    path('validate/', include([
        path('email/', validate_email, name='validate_email'),
        path('user/', validate_user, name='validate_user'),
        path('email-registered/', validate_email_registered, name='validate_email_registered'),
    ]))
]