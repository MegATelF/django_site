from django.urls import path

from . import views

urlpatterns = [
    path('', views.starting_page, name="starting-page"),
    path('about/', views.about_page, name="about-page"),
    path('contacts/', views.contacts_page, name="contacts-page"),
    path("content/<slug:slug>", views.post_detail, name="post_detail_page"),
]
