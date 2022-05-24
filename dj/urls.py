"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from short_links.views import main, list, add_short_link, url_info, redir_to, del_short_link

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^list/$', list, name='list'),
    url(r'^add_short_link/$', add_short_link, name='add_short_link'),
    url(r'^del_short_link/(?P<id>\d+)/$', del_short_link, name='del_short_link'),
    url(r'^url_info/(?P<id>\d+)/$', url_info, name='url_info'),
    url(r'^admin/', admin.site.urls),
    url(r"^(?P<short_url>[\d\w]+)/$", redir_to, name='redir_to'),
]
