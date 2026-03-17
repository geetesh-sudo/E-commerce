from django.shortcuts import render, redirect
from .models import Products
from authen.models import CartModel
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def home(request):
    if request.user.is_authenticated:
        cartproductscount = CartModel.objects.filter(host=request.user).count()
    else:
        cartproductscount = 0

    nomatch = False

    if 'trending' in request.GET:
        all_products = Products.objects.filter(trending=True)

    elif 'offer' in request.GET:
        all_products = Products.objects.filter(offer=True)

    elif 'q' in request.GET:
        q = request.GET.get('q')
        all_products = Products.objects.filter(
            Q(pname__icontains=q) | Q(pdesc__icontains=q)
        )
        if not all_products.exists():
            nomatch = True

    else:
        all_products = Products.objects.all()

    return render(request, 'home.html', {
        'all_products': all_products,
        'cartproductscount': cartproductscount,
        'nomatch': nomatch
    })


@login_required
def addtocart(request, pk):
    product = Products.objects.get(id=pk)

    try:
        cp = CartModel.objects.get(pname=product.pname, host=request.user)
        cp.quantity += 1
        cp.totalprice += product.price
        cp.save()
    except:
        CartModel.objects.create(
            pname=product.pname,
            price=product.price,
            pcategory=product.pcategory,
            quantity=1,
            totalprice=product.price,
            host=request.user
        )

    return redirect('home')


@login_required(login_url='login_')
def cart(request):
    cartproducts = CartModel.objects.filter(host=request.user)
    cartproductscount = cartproducts.count()

    TA = sum(i.totalprice for i in cartproducts)

    return render(request, 'cart.html', {
        'cartproducts': cartproducts,
        'TA': TA,
        'cartproductscount': cartproductscount
    })


@login_required
def remove(request, pk):
    CartModel.objects.get(id=pk).delete()
    return redirect('cart')

def add(request,pk):
    cproduct=CartModel.objects.get(id=pk)
    cproduct.quantity+=1
    cproduct.totalprice+=cproduct.price
    cproduct.save()
    return redirect('cart')

def sub(request,pk):
    cproduct=CartModel.objects.get(id=pk)
    if cproduct.quantity>1:
        cproduct.quantity-=1
        cproduct.totalprice-=cproduct.price
        cproduct.save()
    else:
        cproduct.save()
    return redirect('cart')

