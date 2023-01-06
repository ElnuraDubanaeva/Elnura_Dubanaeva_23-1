from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from users.forms import LoginForm, RegisterForm
from django.contrib.auth.views import LoginView, LogoutView, FormView


# Create your views here.
class LoginCBV(LoginView, FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = '/products/'

    def get_context_data(self, **kwargs):
        return {
            'form': kwargs['form']
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(
            form=self.form_class
        ))

    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user=user)
                return redirect(self.success_url)
            else:
                form.add_error('username', 'bad request!')

        return render(request, self.template_name, self.get_context_data(
            form=form
        ))


# def login_view(request):
#     if request.method == 'GET':
#         context = {
#             'form': LoginForm
#         }
#         return render(request, 'users/login.html', context=context)
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data.get('username'),
#                 password=form.cleaned_data.get('password')
#             )
#             if user:
#                 login(request, user=user)
#                 return redirect('/products/')
#             else:
#                 form.add_error('username', 'bad request!')
#
#         return render(request, 'users/login.html', context={
#             'form': form
#         })

class LogoutCBV(LogoutView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/products/')


# def logout_view(request):
#     logout(request)
#     return redirect('/products/')


class SignUpCBV(CreateView, FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = '/products/'

    def get_context_data(self, **kwargs):
        return {
            'form': kwargs['form'],
            'user': kwargs['user']
        }

    def get(self, request, **kwargs):
        return render(request, self.template_name, self.get_context_data(
            form=self.form_class,
            user=None if request.user.is_anonymous else request.user
        ))

    def post(self, request, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password2')
                )
                login(request, user)
                return redirect(self.success_url)
            else:
                form.add_error('password2', 'bad request!')
        return render(request, self.template_name, self.get_context_data(
            form=form,
            user=None if request.user.is_anonymous else request.user
        ))

#
# def register_view(request):
#     if request.method == 'GET':
#         context = {
#             'form': RegisterForm,
#             'user': None if request.user.is_anonymous else request.user
#         }
#         return render(request, 'users/register.html', context=context)
#     if request.method == 'POST':
#         form = RegisterForm(data=request.POST)
#
#         if form.is_valid():
#             if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
#                 user = User.objects.create_user(
#                     username=form.cleaned_data.get('username'),
#                     password=form.cleaned_data.get('password2')
#                 )
#                 login(request, user)
#                 return redirect('/products/')
#             else:
#                 form.add_error('password2', 'bad request!')
#         return render(request, 'users/register.html', context={
#             'form': form,
#             'user': None if request.user.is_anonymous else request.user
#         })
