from django.urls import path 

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('product',views.gallery,name='product'),
    path('review',views.review,name='review'),
    path('contact',views.contact,name='contact'),
    path('',views.datastore,name="datastore")
]
