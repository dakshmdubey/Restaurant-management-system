from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem,Order
from django.db.models import Q,Sum,Count
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Table
from django.utils import timezone

def home(request):
    return render(request,'home.html')
def menu(request):
    foods = MenuItem.objects.all()
    return render(request, 'menu.html', {
        'foods': foods
    })
def update_menu(request, id):
    item = get_object_or_404(MenuItem, id=id)

    if request.method == "POST":
        item.name = request.POST['name']
        item.price = request.POST['price']
        item.save()
        return redirect('menu')

    return render(request, 'update_menu.html', {'item': item})

def delete_menu(request, id):
    item = get_object_or_404(MenuItem, id=id)
    item.delete()
    return redirect('menu')

def place_order(request):
    foods = MenuItem.objects.all()
    tables = Table.objects.filter(status='Available')

    if request.method == "POST":
        customer_name = request.POST['customer_name']
        food_id = request.POST['food_item']
        quantity = request.POST['quantity']
        table_id = request.POST['table']

        food = MenuItem.objects.get(id=food_id)
        table = Table.objects.get(id=table_id)

        Order.objects.create(
            customer_name=customer_name,
            food_item=food,
            quantity=quantity,
            table=table
        )

        table.status = 'Occupied'
        table.save()

        return redirect('menu')

    return render(request, 'place_order.html', {
        'foods': foods,
        'tables': tables
    })
def order_list(request):
    orders = Order.objects.all().order_by('-order_date')

    search = request.GET.get('search')
    status = request.GET.get('status')

    if search:
        orders = orders.filter(
            Q(customer_name__icontains=search) |
            Q(food_item__name__icontains=search)
        )

    if status:
        orders = orders.filter(status=status)

    total_revenue = 0
    pending = 0
    preparing = 0
    ready = 0
    delivered = 0

    for order in orders:
        order.total = order.food_item.price * order.quantity
        total_revenue += order.total

        if order.status == "Pending":
            pending += 1
        elif order.status == "Preparing":
            preparing += 1
        elif order.status == "Ready":
            ready += 1
        elif order.status == "Delivered":
            delivered += 1

    return render(request, 'order_list.html', {
        'orders': orders,
        'total_revenue': total_revenue,
        'pending': pending,
        'preparing': preparing,
        'ready': ready,
        'delivered': delivered,
    })

def download_bill(request, id):
    order = get_object_or_404(Order, id=id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = (
        f'attachment; filename="bill_{order.id}.pdf"'
    )

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 18)
    p.drawString(180, 800, "Restaurant Bill")

    p.setFont("Helvetica", 12)
    p.drawString(50, 740, f"Customer: {order.customer_name}")
    p.drawString(50, 710, f"Food Item: {order.food_item.name}")
    p.drawString(50, 680, f"Price: ₹{order.food_item.price}")
    p.drawString(50, 650, f"Quantity: {order.quantity}")
    p.drawString(50, 620, f"Total: ₹{order.total_price}")
    p.drawString(50, 590, f"Status: {order.status}")
    p.drawString(
        50,
        560,
        f"Date: {order.order_date.strftime('%d-%m-%Y %I:%M %p')}"
    )

    p.drawString(50, 500, "Thank you for visiting our restaurant!")

    p.showPage()
    p.save()

    return response

def table_list(request):
    tables = Table.objects.all()
    return render(request, 'table_list.html', {'tables': tables})

def sales_report(request):
    filter_type = request.GET.get('filter')
    selected_date = request.GET.get('date')

    orders = Order.objects.all().order_by('-order_date')

    if filter_type == 'today':
        today = timezone.now().date()
        orders = orders.filter(order_date__date=today)

    if selected_date:
        orders = orders.filter(order_date__date=selected_date)

    total_orders = orders.count()

    total_revenue = sum(
        order.food_item.price * order.quantity
        for order in orders
    )

    delivered_orders = orders.filter(
        status='Delivered'
    ).count()

    pending_orders = orders.filter(
        status='Pending'
    ).count()

    most_ordered = (
    orders.values('food_item__name')
    .annotate(total=Count('food_item'))
    .order_by('-total')
    .first()
    )

    average_order_value = (
        total_revenue / total_orders
        if total_orders > 0 else 0
    )

    context = {
        'orders': orders,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'delivered_orders': delivered_orders,
        'pending_orders': pending_orders,
        'most_ordered': most_ordered,
        'average_order_value': average_order_value,
        'selected_date': selected_date,
    }

    return render(request, 'sales_report.html', context)
# Create your views here.
