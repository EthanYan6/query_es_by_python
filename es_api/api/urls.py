from django.conf.urls import url

from . import views

# urlpatterns是被django自动识别的路由列表变量
urlpatterns = [
    # url(路径, 视图)
    url(r'^matchall/(?P<index>[a-z_]+)/$', views.matchall),
]