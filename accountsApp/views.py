from django.shortcuts import render, redirect
from django.http import HttpResponse
from accountsApp.models import *
from .forms import OrderForm
from django.forms import inlineformset_factory
from .filter import OrderFilter

# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    pending_orders = orders.filter(status='pending').count()
    delivered_orders = orders.filter(status='delivered').count()
    context = {'orders': orders, 'customers': customers
               , 'total_customers': total_customers, 'total_orders': total_orders
               , 'pending_orders': pending_orders, 'delivered_orders': delivered_orders}
    return render(request, '../templates/dashboard.html', context)

#def dashboard(request):
#    return render(request, 'accountsApp/dashboard.html')


def products(request):
    products = Product.objects.all()
    return render(request, '../templates/products.html', {'products': products})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    myFilter = OrderFilter()
    context = {'customer': customer, 'orders': orders, 'myFilter': myFilter}
    return render(request, '../templates/customer.html', context)

def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #print('Printing POST:  ', request.POST)
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, '../templates/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, '../templates/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, '../templates/delete.html', context)