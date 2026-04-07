from django.conf.urls import url
from storeapp import views

# TEMPLATE TAGGING
app_name = 'storeapp'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^info/', views.bookinfo, name='bookinfo'),
]