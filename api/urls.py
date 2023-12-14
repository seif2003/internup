from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^company/$', views.addCompany),
    url(r'^companies/$', views.companies),
    url(r'^offers/$', views.offers),
    url(r'^industries/$', views.industries),
    url(r'^technologies/$', views.technologies),
    url(r'^socialmedias/$', views.socialmedias),
    url(r'^locations/$', views.locations),
    url(r'^version/(?P<channel>\w+)/$', views.version),
    url(r'^company/(?P<id>\d+)/$', views.company),
    url(r'^offer/$', views.offer),
    url(r'^offer/(?P<id>\d+)/$', views.offer),
    url(r'^report_company/$', views.report_company),
    url(r'^report_offer/$', views.report_offer),
]
