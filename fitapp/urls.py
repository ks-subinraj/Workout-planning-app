from django.urls import path
from . import views
urlpatterns = [
    path('',views.main_page_view,name='main_page'),
    path('<slug:slug>',views.main_page_view,name='main_page_view'),
]