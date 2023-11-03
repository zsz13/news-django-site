import os.path
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import *
import json

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]
file_path = os.path.join('currency_rate_weather.json')


class NewsHome(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        data_usd, data_eur, data_rub, weather = read_json(file_path)
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['data_usd'] = data_usd
        context['data_eur'] = data_eur
        context['data_rub'] = data_rub
        context['weather_data'] = weather
        context['city'] = 'Алматы'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        data_usd, data_eur, data_rub, weather = data['usd_rate'], data['eur_rate'], data['rub_rate'], data['weather_data']
    return data_usd, data_eur, data_rub, weather


# def index(request):
#     data_usd, data_eur, data_rub, weather = read_json(file_path)
#     posts = News.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#         'data_usd': data_usd,
#         'data_eur': data_eur,
#         'data_rub': data_rub,
#         'weather_data': weather,
#         'city': 'Алматы',
#     }
#
#     return render(request, 'news/index.html', context=context)


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'news/add_post.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data_usd, data_eur, data_rub, weather = read_json(file_path)
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление поста'
        context['data_usd'] = data_usd
        context['data_eur'] = data_eur
        context['data_rub'] = data_rub
        context['weather_data'] = weather
        context['city'] = 'Алматы'
        return context
# def add_post(request):
#     data_usd, data_eur, data_rub, weather = read_json(file_path)
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'news/add_post.html', {'form': form, 'menu': menu, 'title': 'Добавление поста', 'data_usd': data_usd, 'data_eur': data_eur, 'data_rub': data_rub, 'weather_data': weather, 'city': 'Алматы'})


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


class ShowPost(DetailView):
    model = News
    template_name = 'news/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        data_usd, data_eur, data_rub, weather = read_json(file_path)
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        context['data_usd'] = data_usd
        context['data_eur'] = data_eur
        context['data_rub'] = data_rub
        context['weather_data'] = weather
        context['city'] = 'Алматы'
        return context
# def show_post(request, post_slug):
#     post = get_object_or_404(News, slug=post_slug)
#     data_usd, data_eur, data_rub, weather = read_json(file_path)
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#         'data_usd': data_usd,
#         'data_eur': data_eur,
#         'data_rub': data_rub,
#         'weather_data': weather,
#         'city': 'Алматы',
#     }
#     return render(request, 'news/post.html', context=context)


def about(request):
    data_usd, data_eur, data_rub, weather = read_json(file_path)
    return render(request, 'news/about.html', {'title': 'О сайте', 'data_usd': data_usd, 'data_eur': data_eur, 'data_rub': data_rub, 'weather_data': weather, 'city': 'Алматы'})


def contact(request):
    return render(request, 'news/contact.html', {'title': 'Обратная связь'})


def categories(request, categoryid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{categoryid}</p>")


class NewsCategory(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        data_usd, data_eur, data_rub, weather = read_json(file_path)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        context['data_usd'] = data_usd
        context['data_eur'] = data_eur
        context['data_rub'] = data_rub
        context['weather_data'] = weather
        context['city'] = 'Алматы'
        return context
# def show_category(request, cat_id):
#     posts = News.objects.filter(cat_id=cat_id)
#     data_usd, data_eur, data_rub, weather = read_json(file_path)
#     if len(posts) == 0:
#         raise Http404()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#         'data_usd': data_usd,
#         'data_eur': data_eur,
#         'data_rub': data_rub,
#         'weather_data': weather,
#         'city': 'Алматы',
#     }
#     return render(request, 'news/index.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')