from django.urls import path

from apps.pages.views import *

app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('category/', category_page_view, name='category'),
    path('blog/', blog_page_view, name='blogs'),
    path('about/', about_page_view, name='about'),
    path('error/', error_page_view, name='error'),
    path('blog-detail/', blog_detail_page_view, name='blog-detail'),
    path('cart/', cart_page_view, name='cart'),
    path('checkout/', checkout_page_view, name='checkout'),
    path('coming-soon/', coming_soon_page_view, name='coming'),
    path('contact/', contact_page_view, name='contact'),
    path('dashboard/', dashboard_page_view, name='dashboard'),
    path('faq/', faq_page_view, name='faq'),
    path('product/', product_page_view, name='product'),
    path('wishlist/', wishlist_page_view, name='wishlist'),
    ]