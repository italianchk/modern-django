from django.conf.urls import include, url
from hello.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home')
]
