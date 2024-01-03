from django.urls import path
from .  import views
from .views import show_10k_filing

urlpatterns = [
    path('', views.home, name='home'),
    path('landing', views.landing, name='landing'),
    path('about', views.about, name='about'),
    path('tenk', views.tenk, name='tenk'),
    path('tenq', views.tenq, name='tenq'),
    path('eightk', views.eightk, name='eightk'),
    path('show-10k/', views.show_10k_filing, name='show-10k'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('delete/<stock_id>', views.delete, name='delete'),
    path('learn', views.learn, name='learn'),


]