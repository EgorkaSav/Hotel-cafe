from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout as auth_logout, authenticate
from .models import Room, Booking
from .forms import BookingForm, LoginForm, ReceiveProductForm, Otgruz
from .models import Room, Blog, Sklad
from .models import MenuItem, Category
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.admin.views.decorators import staff_member_required

#import stripe
""" from django.conf import settings                             убрать комментарии когда будет договор с провайдером платежей

stripe.api_key = settings.STRIPE_SECRET_KEY

def charge(request):
    if request.method == 'POST':
        # Получение данных карты и суммы платежа
        token = request.POST['stripeToken']
        amount = 500 # Сумма

        try:
            # Создание платежа
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description='Example charge',
                source=token,
            )
            # Предполагаем, что платеж прошел успешно:
            booking = Booking.objects.get(id=booking_id)
            if booking.is_paid = True:
                booking.save()
                return render(request, 'payment_success.html', {'booking': booking})
            else:
                booking.save()
                # Возможно, вы хотите добавить сообщение или перенаправление
                return render(request, 'payment_cancelled.html', {'booking': booking})
        except stripe.error.StripeError as e:
            return JsonResponse({'error': str(e)}, status=403)

    return JsonResponse({'error': 'Wrong request'}, status=400) """





def home(request):
# логика для главной страницы
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

""" def blog_list(request):
    
    print (blogs) """
    

def menu(request):
# логика для страницы меню
    categories = Category.objects.all()
    return render(request, 'menu.html', {'categories': categories})
    """ menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items}) """

def rooms(request):
# логика для страницы информации о номерах
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})


@login_required(login_url='register')
def book_room(request):
    print(request.POST)    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            room_id = request.POST.get('room') # Получаем room_id из запроса
            room = Room.objects.get(id=room_id) # Получаем объект комнаты по room_id
            check_in_date = request.POST.get('check_in_date')
            check_out_date = request.POST.get('check_out_date')
            existing_bookings = Booking.objects.filter(room=room, check_out_date__gt=check_in_date, check_in_date__lt=check_out_date)
            if existing_bookings.exists():
                return render(request, 'booking_error.html', {'message':'Выбраные даты заняты, выберите другие'})
            else:
                booking = form.save(commit=False)
                booking.room = room # Устанавливаем комнату для бронирования
                booking.save()
                return HttpResponseRedirect(reverse('booking_success')) # Перенаправляем на страницу успешного бронирования
    else:
        form = BookingForm()
    return render(request, 'rooms.html', {'form': form})
    

@login_required(login_url='register')
def profile(request):
    user = request.user
    bookings = user.booking_set.all() # Получить все бронирования пользователя
    return render(request, 'profile.html', {'user': user, 'bookings': bookings})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def booking_success(request):
    return render (request, 'booking_success.html')


@staff_member_required
def sklad_view(request):
    products = Sklad.objects.all()
    form_a = ReceiveProductForm(request.POST or None)
    form_b = Otgruz(request.POST or None)
    if 'Receive' in request.POST:
        form_a = ReceiveProductForm(request.POST)
        form_b = Otgruz()
        if form_a.is_valid():
            product_name = form_a.cleaned_data['prod_name']
            quantity = form_a.cleaned_data['kol_vo']
            existing_product = Sklad.objects.filter(prod_name=product_name).first()
            if existing_product:            
                existing_product.kol_vo += quantity
                existing_product.save()
            else:            
                form_a.save()
            return redirect ('sklad')
    elif 'Otgruz' in request.POST:
        form_a = ReceiveProductForm()
        form_b = Otgruz(request.POST)
        if form_b.is_valid():
            product_name = form_b.cleaned_data['prod_name']
            quantity = form_b.cleaned_data['kol_vo']
            existing_product = Sklad.objects.filter(prod_name=product_name).first()
            if existing_product:            
                existing_product.kol_vo -= quantity
                existing_product.save()            
            return redirect ('sklad')

    return render(request, 'sklad.html', {'products': products, 'form_a': form_a, 'form_b': form_b})
   
