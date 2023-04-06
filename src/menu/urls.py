from django.urls import path
from .views import MenuPageView, get_template

urlpatterns = [
    path('menu/<slug:slug>/', MenuPageView.as_view(), name='menu'),
    path('menu1/<slug:slug>/', get_template, name='menu1'),
]
