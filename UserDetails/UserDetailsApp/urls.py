"""
__author__ = "Rahul kumar"
__version__ ="1.0"
__date__ = "May 7 15:48:15 2019"
__copyright__ = "©2019 rahul_kumar"
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^users$', views.UserDetails.as_view(), name='users'),
    url(r'^users/(\d)$', views.UserQueryWithId.as_view(), name='users_by_id'),
    # url(r'^users/(?P<page>^[0-9]+$)/(?P<limit>^[0-9]+$)/(?P<name>[\w.-]+)/(?P<sort>[\w.-]+)', views.UserSelectionDetail.as_view(), name='user_selection'),
    ]