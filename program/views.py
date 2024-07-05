from django.shortcuts import render, redirect
from .models import UserOrderModel
from .forms import UserOrderForm


def index(request):
    return render(request, 'program/index.html')


def order(request):
    payment = UserOrderModel.objects.all()
    form = UserOrderForm()
    context = {'payment': payment, 'form': form}
    if request.method == "POST":
        form = UserOrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request, 'program/order.html', context=context)
