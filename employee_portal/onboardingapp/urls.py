from django.conf.urls import url
from onboardingapp import views

app_name = 'onboardingapp'

urlpatterns = [
    url(r'^register/', views.register, name = 'register'),
    url(r'^preview/(?P<user_obj>\d+)/', views.preview, name = 'preview'), 
]

    