from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('politics/', politics, name='politics'),
    path('economy/', economy, name='economy'),
    path('sport/', sport, name='sport'),
    path('technologies/', technologies, name='technologies'),
    path('world-events/', world_events, name='world-events'),
    path('entertainments/', entertainments, name='entertainments'),
    path('celebrities/', celebrities, name='celebrities'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]