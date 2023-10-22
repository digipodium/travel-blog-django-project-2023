from django.urls import path
from . import views
urlpatterns = [
    path('article/form', views.article_form, name='article_form'),
    # htmx urls to process the form
    path('htmx/article/process', views.process_article, name='process_article'),
    path('htmx/category/process', views.process_category, name='process_category'),
    path('htmx/tag/process', views.process_tag, name='process_tag'),
    # htmx url to load list
    path('htmx/article/list', views.article_list, name='article_list'),
    path('htmx/category/list', views.category_list, name='category_list'),
    path('htmx/tag/list', views.tag_list, name='tag_list'),
]