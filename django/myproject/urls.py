from django.conf.urls import include, url
from django.contrib import admin
import pytoon.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #이부분이 동작하는 코드
    #url(r'^keyboard/', 'pytoon.views.keyboard'),
    #url(r'^message' , 'pytoon.views.answer'),

    url(r'^keyboard/', pytoon.views.keyboard),


]
