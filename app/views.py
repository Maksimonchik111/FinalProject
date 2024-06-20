from django.shortcuts import render, redirect
from .models import News
from .forms import UserRegisterForm, UserLoginForm, NewsCreateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator


def index_view(request):
    news = News.objects.all()

    return render(request, 'app/index.html', {'newses': news})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'app/user_register.html',{'form':form})


class CustomLoginView(LoginView):
    template_name = 'app/user_login.html'
    authentication_form = UserLoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('index')


def user_logout_view(request):

    logout(request)
    return redirect('index')


def news_detail_view(request, pk):
    detail_news = News.objects.get(id=pk)

    return render(request, 'app/detail.html',{'detail_news': detail_news})


@user_passes_test(lambda u: u.is_authenticated and u.is_superuser, login_url='/login/')
def news_create(request):
    if request.method == 'POST':
        form = NewsCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')

    form = NewsCreateForm()

    return render(request, 'app/news_create.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser, login_url='/login/')
def news_delete(request, pk):
    news = News.objects.get(id=pk)
    news.delete()
    return redirect('index')

