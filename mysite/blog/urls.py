from django.conf.urls import url
from django.urls import include, path

# import all the views that arre required to diplay all the pages for a blog post
from .views import showMainPage, showIndividualPost

# build the url patterns that will be used for redirection
urlpatterns = [
    path('' showMainPage, name='displayMainPage'),
    path('/<int:id>', showIndividualPost, name='showIndividualPost'),
]
