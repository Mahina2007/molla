from django.urls import path

from apps.accounts.views import *

app_name = 'apps.accounts'

urlpatterns = [
    path('login/', login_page_view, name='login'),
]