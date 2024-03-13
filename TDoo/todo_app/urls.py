from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.ListTODOView.as_view()),
    path('add/', views.AddTODOView.as_view()),
    path('detail/<int:pk>/', views.DetailTODOView.as_view()),
    path('delete/<int:id>/', views.DeleteTODOView.as_view()),
    path('update/<int:id>/', views.UpdateTODOView.as_view()),
]