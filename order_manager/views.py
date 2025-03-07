from django.shortcuts import render, HttpResponseRedirect
from .models import Order
from .const import MENU
import re


def index(request):
    context = {
        'message': 'Выберите раздел меню'
    }
    return render(request, 'index.html', context)


def order_list(request):
    orders = Order.objects.all()
    prices = [int(order.total_price) for order in orders if order.status == 'оплачено']
    rev = sum(prices)
    context = {'message': 'Текущие заказы', 'orders': orders, 'rev': rev}
    if request.method == 'POST':
        param = request.POST['param']
        try:
            int_param = int(param)
            query = orders.filter(table_number=int_param)
        except ValueError:
            str_param = param
            query = orders.filter(status=str_param)
        if not query:
            context['message'] = 'Заказ не найден!'
        else:
            context['orders'] = query
    return render(request, 'main.html', context)


def add_order(request):
    if request.method == 'POST':
        table_number = request.POST['table_number']
        items = request.POST['items']
        if table_number and items:
            prices = [int(i) for i in re.findall(r'\b\d+\b', items)]
            total_price = sum(prices)
            status = 'в ожидании'
            Order.objects.create(
                table_number=table_number,
                items=items,
                total_price=total_price,
                status=status
            )
            return HttpResponseRedirect('/main/')
        else:
            return HttpResponseRedirect('/add/')
    else:
        context = {
            'message': 'Добавить заказ',
            'menu': MENU,
        }
        return render(request, 'add.html', context)


def change_status(request, order_id):
    current_status = request.POST['current_status']
    order = Order.objects.get(id=order_id)
    order.status = current_status
    order.save()
    return HttpResponseRedirect('/main/')


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return HttpResponseRedirect('/main/')


def finish_working_day(request):
    Order.objects.all().delete()
    return HttpResponseRedirect('/main/')
