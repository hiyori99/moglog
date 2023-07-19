from django.shortcuts import render, get_object_or_404, redirect
from .models import Shop, Menu
from .forms import ShopForm, MenuForm

def home(request):
    shops = Shop.objects.all()
    print(shops)
    return render(request, 'mymapp/home.html', {'shops': shops})

def shop_detail(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    return render(request, 'mymapp/shop_detail.html', {'shop': shop})

def add_shop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mymapp:home')
    else:
        form = ShopForm()
    return render(request, 'mymapp/add_shop.html', {'form': form})

def edit_shop(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)

    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('mymapp:home')
    else:
        form = ShopForm(instance=shop)

    return render(request, 'mymapp/edit_shop.html', {'form': form})

def delete_shop(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    shop.delete()
    return redirect('mymapp:home')

def add_menu(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)

    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.shop = shop
            form.save()
            return redirect('mymapp:shop_detail', shop_id=shop_id)
    else:
        form = MenuForm()

    return render(request, 'mymapp/add_menu.html', {'form': form, 'shop_id': shop_id, 'shop': shop})
