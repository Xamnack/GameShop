import datetime

from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from gameApp.models import GameLibrary, Game, HistoryPay
from gameApp.views import Library, CartUser
from userApp.forms import *
from userApp.models import *


def LogIn(request):
    invalid = 'Неверный логин или пароль'
    if request.method == 'POST':
        form = loginForm(request.POST)
        if 'LogIn' in request.POST:
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect("/")
                    else:
                        return render(request, 'templates/LoginForm.html', {'log_form': form, 'invalid': invalid})
                else:
                    return render(request, 'templates/LoginForm.html', {'log_form': form, 'invalid': invalid})
    else:
        form = loginForm()
    return render(request, 'templates/LoginForm.html', {'log_form': form})


def LogOut(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    if request.method == 'POST':
        user_form = regForms(request.POST)
        if 'regbut' in request.POST:
            if user_form.is_valid():
                new_user = user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password2'])
                new_user.save()
                return redirect("/")
    else:
        user_form = regForms()
    return render(request, 'templates/RegistrationForm.html', {'reg_form': user_form})


class ProfileView(View):
    def getProfile(request, user):
        return render(request, 'templates/profile.html', {'game_list': Library.get(request)})

    def editProfile(request, user):

        if request.method == 'POST':
            user_form = UserEditForm(instance=request.user, data=request.POST)
            profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
        else:
            user_form = UserEditForm(instance=request.user)
            profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'templates/editProfile.html', {'user_form': user_form, 'profile_form': profile_form})

    def getCart(request, user):
        games_in_cart = CartUser.get(request)
        sum_games_in_cart = games_in_cart.aggregate(price=Sum("game__price"))
        if 'buy' in request.POST:
            for i in games_in_cart:
                lib = GameLibrary()
                lib.user = request.user
                lib.game = i.game
                history_pay = HistoryPay()
                history_pay.game = i.game
                history_pay.user = request.user
                history_pay.datePay = datetime.datetime.now()
                HistoryPay.save(history_pay)
                GameLibrary.save(lib)
                game = Game.objects.get(id=i.game.id)
                game.count_download += 1
                game.save()
            games_in_cart.delete()
        if 'delete' in request.POST:
            game = request.POST.getlist('games')
            for pk in game:
                var = games_in_cart.filter(game__pk=pk)
                var.delete()
        return render(request, 'templates/cart.html', {'games': games_in_cart, 'sum_cart': sum_games_in_cart})

    def getHistoryPay(request, user):
        hp = HistoryPay.objects.filter(user=request.user)
        return render(request, 'templates/HistoryPay.html', {'HistoryPay': hp})

