from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name="dashboard"),

    path('workers/', views.workers_list, name="workers"),
    path('plans/', views.plans_list, name="plans"),

    path('add-worker/', views.add_worker, name="add_worker"),
    path('add-plan/', views.add_plan, name="add_plan"),

    path('edit-worker/<int:id>/', views.edit_worker, name="edit_worker"),
    path('delete-worker/<int:id>/', views.delete_worker, name="delete_worker"),

    path('edit-plan/<int:id>/', views.edit_plan, name="edit_plan"),
    path('delete-plan/<int:id>/', views.delete_plan, name="delete_plan"),
]