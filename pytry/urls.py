from django.conf.urls import url
from django.contrib import admin
from .views import comment_form,init_comment_form,comment_detail

urlpatterns = [
    url(r'^init_form/',init_comment_form),
    url(r'^form/',comment_form),
    url(r'^detail/',comment_detail)
    # url(r'^(?P<right>\d+)/$',comment_comment_response),
    # url(r'^comment/$',init_comment_response),
]