from django.conf.urls import url
from django.urls import include, path

# import all the views that arre required to diplay all the pages for a blog post
from .views import showMainPage, showAboutPage, showIndividualPost, showContactPage, addCommentPage

# build the url patterns that will be used for redirection
urlpatterns = [
    path('', showMainPage, name='showMainPage'),
    path('about/', showAboutPage, name='showAboutPage'),
    path('<int:id>/', showIndividualPost, name='showIndividualPost'),
    path('contact/', showContactPage, name='showContactPage'),
    path('<int:id>/comment/', addCommentPage, name='addCommentPage'),
]
