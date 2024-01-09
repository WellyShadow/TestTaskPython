"""Module with urls."""
from django.urls import path

from . import views

urlpatterns = [
    path('verify_email/', views.verify_email, name='verify_email'),  # post
    path('create-email-result/', views.create_email_result),  # post
    path('get-email-result/<int:email_id>/', views.get_email_result),  # get
    path('update-email-result/<int:email_id>/', views.update_email_result),  # put
    path('delete-email-result/<int:email_id>/', views.delete_email_result),  # delete
    path('get-all-email-result/', views.get_all_email_result),  # get
]
