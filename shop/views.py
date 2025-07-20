from django.shortcuts import render
from .models import Product, Category, Tag
from django.db.models import Q

def product_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    tag_id = request.GET.get('tag')

    products = Product.objects.all()

    # Apply search filter
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    # Filter by category
    if category_id:
        products = products.filter(category_id=category_id)

    # Filter by tag
    if tag_id:
        products = products.filter(tags__id=tag_id)

    # Fetch categories and tags by filters
    categories = Category.objects.all()
    tags = Tag.objects.all()

    # Display all products based on the given filters and tags
    return render(request, 'shop/product_list.html', {
        'products': products,
        'categories': categories,
        'tags': tags,
        'query': query,
        'selected_category': category_id,
        'selected_tag': tag_id,
    })
