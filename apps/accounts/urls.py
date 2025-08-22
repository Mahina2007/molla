from django.urls import path

from apps.accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', login_page_view, name='login'),
]