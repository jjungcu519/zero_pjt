from django.shortcuts import render
import random

# Create your views here.

def root(request):
    return render(request, 'root.html')

def sayhi(request):
    username = 'JA519'

    context = {
        'name' : username
    }

    return render(request, 'sayhi.html', context)

def menus(request):
    meals = ['🍣 스시', '🍜라면', '🍝 파스타', '🍔 햄버거', '🌭 핫도그', '🌮 타코', '🥙 부리또', '🍕 피자', '🍟 감자튀김', '🍖 고기']
    pick_today = random.choice(meals)

    context = {
        'pick' : pick_today
    }
    return render(request, 'menus.html', context)

def lotto(request):
    pick_lotto = random.sample(range(1,46), 6)

    context = {
        'lotto' : pick_lotto
    }
    return render(request, 'lotto.html', context)

def cube(request, number):
    result = number ** 3
    context = {
        'cube' : result,
        'number' : number,
    }

