from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, login_view, ticket_view
from . import views

urlpatterns = [

    path('', signup_view, name='signup'),
    path('tickets/', ticket_view, name='tickets'),
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-ticket/', views.add_ticket, name='add-ticket'),
    path('tickets/edit/<int:id>/', views.edit_ticket,name='edit'),
]
