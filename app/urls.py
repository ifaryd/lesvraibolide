from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name='accueil'),
    path('accueil', views.index, name='accueil'),
    path('contact', views.contact, name='contact')

    #path('<slug:lang>/', views.index, name='index'),

    #path('<slug:lang>/contact', views.contact, name='contact'),
    
    #path('<slug:lang>/predication/<int:predid>', views.predications_detail, name="predication"),
    
]