from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, generate_pass, password_reset_view, verify_email_view

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/new_pass', generate_pass, name='new_pass'),
    path('verification/<int:key>/', verify_email_view, name='verification'),
    path('forgot_password/', password_reset_view, name='password_reset'),

]