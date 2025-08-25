from django.shortcuts import render

def home_page_view(request):
    return render(request, 'home.html')

def category_page_view(request):
    return render(request, 'products/category.html')

def blog_page_view(request):
    return render(request, 'blogs/blog-list.html')

def about_page_view(request):
    return render(request, 'products/about.html')

def error_page_view(request):
    return render(request, 'details/404.html')

def blog_detail_page_view(request):
    return render(request, 'blogs/blog-detail.html')

def cart_page_view(request):
    return render(request, 'products/cart.html')

def checkout_page_view(request):
    return render(request, 'products/checkout.html')

def coming_soon_page_view(request):
    return render(request, 'details/coming-soon.html')

def contact_page_view(request):
    return render(request, 'details/contact.html')

def dashboard_page_view(request):
    return render(request, 'auth/dashboard.html')

def faq_page_view(request):
    return render(request, 'details/faq.html')

def product_page_view(request):
    return render(request, 'details/product-detail.html')

def wishlist_page_view(request):
    return render(request, 'products/wishlist.html')


