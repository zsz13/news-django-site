from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from exchange_rate import get_currency_rate
from weather import get_weather
from .models import *
from dnews.constants import constants

# usd_url = "https://www.google.com/search?q=курс+доллара+к+тенге"
# current_usd_rate = get_currency_rate(usd_url)
# eur_url = "https://www.google.com/search?q=курс+евро+к+тенге"
# current_eur_rate = get_currency_rate(eur_url)
# rub_url = "https://www.google.com/search?q=курс+рубля+к+тенге"
# current_rub_rate = get_currency_rate(rub_url)
# api_key = '1cbb43ff0362f2c578b05fe571c1ea68'
# city = 'Almaty'
# weather_data = get_weather(api_key, city)

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]


def index(request):
    # global usd_url
    # global current_usd_rate
    # global eur_url
    # global current_eur_rate
    # global rub_url
    # global current_rub_rate
    # global api_key
    # global city
    # global weather_data
    posts = News.objects.all()
    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,
        'dataUSD': constants['usd_rate'],
        'dataEUR': constants['eur_rate'],
        'dataRUB': constants['rub_rate'],
        'weather_data': constants['weather_data'],
        # 'dataUSD': current_usd_rate,
        # 'dataEUR': current_eur_rate,
        # 'dataRUB': current_rub_rate,
        # 'weather_data': weather_data,
        'city': 'Алматы',
        'menu': menu,
    }

    return render(request, 'news/index.html', context=context)


def politics(request):
    return HttpResponse("Политика")


def economy(request):
    return HttpResponse("Экономика")


def sport(request):
    return HttpResponse("Спорт")


def technologies(request):
    return HttpResponse("Технологии")


def world_events(request):
    return HttpResponse("Мировые события")


def entertainments(request):
    return HttpResponse("Развлечения")


def celebrities(request):
    return HttpResponse("Знаменитости")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_slug):
    global usd_url
    global current_usd_rate
    global eur_url
    global current_eur_rate
    global rub_url
    global current_rub_rate
    global api_key
    global city
    global weather_data
    post = get_object_or_404(News, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
        'dataUSD': current_usd_rate,
        'dataEUR': current_eur_rate,
        'dataRUB': current_rub_rate,
        'weather_data': weather_data,
        'city': 'Алматы',
    }
    return render(request, 'news/post.html', context=context)


def about(request):
    return render(request, 'news/about.html', {'title': 'О сайте'})


def contact(request):
    return render(request, 'news/contact.html', {'title': 'Обратная связь'})


def categories(request, categoryid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{categoryid}</p>")


def show_category(request, cat_id):
    global usd_url
    global current_usd_rate
    global eur_url
    global current_eur_rate
    global rub_url
    global current_rub_rate
    global api_key
    global city
    global weather_data
    posts = News.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
        'dataUSD': current_usd_rate,
        'dataEUR': current_eur_rate,
        'dataRUB': current_rub_rate,
        'weather_data': weather_data,
        'city': 'Алматы',
        'menu': menu
    }
    return render(request, 'news/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
