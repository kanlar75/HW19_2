import random

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from .models import User
from .forms import UserRegisterForm, UserProfileForm
from django.core.mail import send_mail
from django.conf import settings


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save()
        self.object.is_active = False
        self.object.verification_key = ''.join([str(random.randint(0, 9)) for _ in range(0, 9)])
        self.object.save()
        send_mail(
            subject='Регистрация',
            message= f'Вы зарегистрировались на нашем сайте. Для подтверждения регистрации перейдите по ссылке: '
                  f'http://127.0.0.1:8000/users/verification/{self.object.verification_key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_pass(request):
    password = User.objects.make_random_password()
    request.user.set_password(password)
    request.user.save()
    send_mail(
        subject='Восстановление пароля',
        message=f'Ваш новый пароль - {password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )

    return redirect(reverse('users:login'))


def verify_email_view(request, key):
    if request.method == 'GET':
        user = User.objects.get(verification_key=int(key))
        user.is_active = True
        user.save()

        context = {
            'object_list': User.objects.filter(verification_key=key)
        }

    return render(request, 'users/verification.html', context)


def password_reset_view(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.POST.get('email'))
        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()
        send_mail(
            subject='Сброс пароля',
            message=f'Вы запросили сброс пароля. Ваш новый пароль: {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.POST.get('email')]
        )
        return redirect('users:login')

    return render(request, 'users/reset_password.html')
