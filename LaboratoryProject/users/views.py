from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib import auth
from django.core.mail import send_mail
from blog.models import Article
from blog.views import article
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm

# Create your views here.
@login_required(login_url='users:login')
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
        articles = Article.objects.filter(user=request.user)
    context = {
        'form': form,
        'articles': articles
    }
    return render(request, 'users/profile.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            data = """
                            Здравствуйте!

                            Спасибо за регистрацию на портале "&copy;Мой Сайт™"

                            --Это автоматическое сообщение, не нужно на него отвечать.
                                """
            send_mail('Добро пожаловать на "&copy;Мой Сайт™"!', data, from_email="misha5555548@yandex.ru",
                      recipient_list=[request.user.email], fail_silently=False)
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                data = """
                Здравствуйте!

                Вы только что вошли в свой аккаунт на портале "&copy;Мой Сайт™"
                Если это были не вы, то мы ничего не можем поделать)))

                --Это автоматическое сообщение, не нужно на него отвечать.
                    """
                send_mail('Добро пожаловать на "&copy;Мой Сайт™"!', data, from_email="",recipient_list = [request.user.email], fail_silently=False)
                return HttpResponseRedirect(reverse('blog:index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))
