from django.urls import path
from demo import views
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<pk>/', views.delete, name='delete'),
    path('edit/', views.edit, name="edit")
]
