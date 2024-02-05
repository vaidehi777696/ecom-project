from django.shortcuts import render
from.models import Products
from django.core.paginator import Paginator

def index(request):
    product_objects=Products.objects.all()
    

    item_value = request.GET.get('item_value')
    if item_value != '' and item_value is not None:
        product_objects = product_objects.filter(title__icontains=item_value)

    
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request,'index.html',{"product_objects":product_objects})