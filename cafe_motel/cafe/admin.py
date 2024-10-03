from django.contrib import admin
from .models import Room, MenuItem, Booking, Profile, Category, Blog

# Регистрация модели Room в административной панели
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price_per_night', 'image')

# Регистрация модели MenuItem в административной панели
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):    
    list_display = ('name', 'description', 'price')

# Регистрация модели Booking в административной панели
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_name','room', 'check_in_date', 'check_out_date', 'contact_info')

    def get_user_username(self, obj):
        return obj.user.username
    
    get_user_username.short_description = 'User'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')

admin.site.register(Category)

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('title','plot', 'img', 'pub_date')
    readonly_fields = ('img',)
    