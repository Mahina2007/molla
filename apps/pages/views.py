from django.shortcuts import render

def category_page_view(request):
    return render(request, 'category.html')

def blog_page_view(request):
    return render(request, 'blog-list.html')

def about_page_view(request):
    return render(request, 'about.html')

def error_page_view(request):
    return render(request, '404.html')

def blog_detail_page_view(request):
    return render(request, 'blog-detail.html')

def cart_page_view(request):
    return render(request, 'cart.html')

def checkout_page_view(request):
    return render(request, 'checkout.html')

def coming_soon_page_view(request):
    return render(request, 'coming-soon.html')

def contact_page_view(request):
    return render(request, 'contact.html')

def dashboard_page_view(request):
    return render(request, 'dashboard.html')

def faq_page_view(request):
    return render(request, 'faq.html')

def product_page_view(request):
    return render(request, 'product-detail.html')

def wishlist_page_view(request):
    return render(request, 'wishlist.html')


