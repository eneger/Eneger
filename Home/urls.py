from django.urls import path
from Home import views

urlpatterns=[
    path('index',views.index,name='index'),
    path('enegerOS',views.enegerOS,name='enegerOS'),
    path('recneger',views.recneger,name='recneger'),
    path('eclokit',views.eclokit,name='eclokit'),
    path('contact',views.contact,name='contact'),
]
