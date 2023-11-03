from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('', NewsHome.as_view(), name='home'),
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
    path('add-post/', AddPost.as_view(), name='add-post'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', NewsCategory.as_view(), name='category'),
]