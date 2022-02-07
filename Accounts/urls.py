from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("sign-up/", views.sign_up, name="sign-up"),
    path("sign-in/", views.sign_in, name="sign-in"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("about/", views.about, name="about"),
    path("viewprofile/<int:user>/", views.viewprofile, name="viewprofile"),

    # activate user email
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),

    # password reset

    path("reset_password/",
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path("reset_password_sent/",
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>",
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path("reset_password_complete/",
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
]
