from django.urls import path
from . import views
urlpatterns = [
    path('',views.main_page_view,name='main_page'),
    path('<slug:slug>',views.main_page_view,name='main_page_view'),
    path('add/',views.add_workout,name='add_workout'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),

]