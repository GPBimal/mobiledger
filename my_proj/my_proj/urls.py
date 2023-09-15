from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("", views.do_login, name="login"),
    path("signup/", views.do_signup, name="signup"),
    path('home/', views.home_view, name='home'),
    path('find/', views.clientfind_view, name='find'),
    path('customer/', views.newclient_view, name='customer'),
    path('statement/', views.ledger_view, name='statement'),
    path('trans/', views.newtrans_view, name='trans'),
    path('daybook/', views.daybook_view, name='daybook'),
    path('renew/', views.renew_view, name='renew'),
    path('backup/', views.backup_view, name='backup'),

    path('clients/', views.do_client_find, name='clients'),
    path('karowar/', views.do_trans_entry, name='karowar'),
]
