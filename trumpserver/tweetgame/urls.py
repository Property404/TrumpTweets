from django.conf.urls import url
from . import views
urlpatterns = [
            url(r'^$', views.index, name='index'),
            url(r'^test', views.test, name="test"),
            url(r'^random', views.random, name="random")
]

