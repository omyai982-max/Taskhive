from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task, Bid


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "budget",
            "deadline",
            "category",
        ]


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]



class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = [
            "amount",
            "message",
        ]