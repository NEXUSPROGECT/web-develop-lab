from audioop import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from users.models import User
from .forms import CommentForm

# Create your views here.

def index(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request,'blog/home.html', context)

def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        form = CommentForm(request.POST)  # Получаем данные из формы

        if form.is_valid():  # Проверяем валидность формы
            if request.user.is_authenticated:  # Проверяем авторизацию пользователя
                comment = form.save(commit=False)  # Сохраняем, но пока не записываем в БД
                comment.article = article  # Присваиваем статью
                comment.user = request.user  # Присваиваем пользователя
                comment.save()  # Сохраняем комментарий в БД
                return redirect('blog:article', article_id=article_id)  # Перенаправление после успешного добавления
            else:
                return redirect('users:login')

    else:
        form = CommentForm()

    context = {
        'article': article,
        'form': form,
        'comments': Comment.objects.filter(article=article)
    }
    return render(request,'blog/article.html', context)

def about(request):
    return render(request,'blog/about.html')

def user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {
        'articles': Article.objects.filter(user=user),
        'user': user
    }
    return render(request,'blog/user.html', context)


