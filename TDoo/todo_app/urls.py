from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.AddTODOView.as_view()),
    path('delete/<int:id>/', views.DeleteTODOView.as_view()),
    path('update/<int:id>/', views.UpdateTODOView.as_view()),
]