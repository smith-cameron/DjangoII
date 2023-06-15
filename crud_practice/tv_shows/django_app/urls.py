from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.dashboard),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:show_id>', views.display),
    path('shows/edit/<int:show_id>', views.edit),
    path('shows/delete/<int:show_id>', views.delete),
]
