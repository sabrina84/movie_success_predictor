from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^input/', TemplateView.as_view(template_name='getInfo.html')),
    #url(r'^getInfo/', TemplateView.as_view(template_name='showRes.html')),

    #url(r'^getInfo/','showRes', name='getInfo')
    #url(r'^getInfo', views.getInfo, name='getInfo'),
    url(r'^getInfo/', views.showRes, name='getInfo'),

]
