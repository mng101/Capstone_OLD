from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.base import TemplateView
from django.contrib import messages
from django.views.generic import (View, TemplateView, ListView,
                                  DetailView, CreateView, DeleteView,
                                  UpdateView, )

from . import forms

from .models import Account

# Create your views here.

class HomePageView(TemplateView):
    template_name = "challenge/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages.info(self.request, "hello http://example.com")
        return context


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("home")
    template_name = "challenge/signup.html"


class TestPageView(TemplateView):
    template_name = 'challenge/test.html'


class ThanksPageView(TemplateView):
    template_name = 'challenge/thanks.html'


# TODO - Compete the AccountUpdateView
#
class AccountUpdateView(UpdateView):
    model = Account
