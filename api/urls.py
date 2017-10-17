from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from catalog import views

urlpatterns = [
    url(r'^authors/$', views.AuthorList.as_view()),
    url(r'^authors/(?P<pk>[0-9]+)/$', views.AuthorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
