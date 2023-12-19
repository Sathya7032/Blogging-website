from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name="index"),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path('blogs/',blogs,name="blogs"),
    path('blogs/category/<slug:url>',category),
    path('blog/<slug:url>',blogSingle),
    path('tutorials/',tutorials,name="tutorials"),
    path('tutorials/posts/<slug:url>',tutorialsPage),
    path('posts/<slug:url>',singleTutorial),
    path('searchresult/', searchresult, name='searchresults'),
    path('search',search,name="search"),
]
