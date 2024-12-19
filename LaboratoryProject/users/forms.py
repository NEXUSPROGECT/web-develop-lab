from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from users.models import User

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'placeholder': 'Ваш ник на портале'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Ваш логин'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Повторите пароль'}))
    class Meta:
        model = User
        fields = ('first_name','username','email','password1','password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ваш логин'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Введите пароль'
    }))
    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={}))
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={}))
    back_image = forms.ImageField(widget=forms.FileInput(attrs={}))

    class Meta:
        model = User
        fields = ('first_name', 'profile_image', 'back_image')