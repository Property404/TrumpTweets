from django.conf.urls import url
from . import views
urlpatterns = [
            url(r'^$', views.index, name='index'),
            url(r'^realorfake', views.realorfake, name='realorfake'),
            url(r'^test', views.test, name="test"),
            url(r'^random', views.random, name="random"),
            url(r'^morerandom', views.random, name="morerandom"),
            url(r'^compare', views.compare,name="compare"),
            url(r'^scoretweet', views.scoretweet, name="scoretweet")
]

