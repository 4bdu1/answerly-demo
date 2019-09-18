from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = UserCreationForm

