from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home_page, name='home_page'),
    path ('categories/', views.categories_page, name='categories_page'),
    path ('all_events/', views.all_events_page, name='all_events_page'),
    path ('event/detail/<int:pk>/', views.event_detail_page, name='event_detail_page'),
    path ('category/events/<slug:slug>/', views.event_by_category_page, name='event_by_category_page'),
    path ('sign-up/', views.sign_up_page, name='sign_up_page'),
    path ('login/', views.login_page, name='login_page'),
    path ('logout/', views.logout_action, name='logout_action')
]