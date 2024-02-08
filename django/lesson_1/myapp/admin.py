from django.contrib import admin
from .models import Customer, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

class CustomerAdministraion(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'registration_date']
    ordering = ['registration_date', '-name'] # сотрировка
    list_filter = ['registration_date' ] #фильтрация
    search_fields = ['phone_number', 'address'] # поиск по полям
    search_help_text = 'Поиск по полю телефону или адресу' 
    
    """Отдельный пользователь."""
    readonly_fields = ['registration_date'] # поля только для чтения

    fieldsets = [
        (None,{
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        ('Подробности', {
                'description': 'Данные пользователя',
                'fields': ['email', 'phone_number','address'],
            },
        ),
        ('Зарегистрирован', {
                'classes': ['collapse'],
                'fields': ['registration_date'],
            }
         ), 
    ]
    
class ProductAdministraion(admin.ModelAdmin):
    list_display = ['name','quantity', 'price']
    ordering = ['-quantity'] # сотрировка
    list_filter = ['price','quantity'] #фильтрация
    search_fields = ['name', 'description'] # поиск по полям
    search_help_text = 'Поиск по полю имя и описание продукта(description)'
    actions = [reset_quantity] # дополнительные опции для работы с данными таблицы помимо удаления


    """Отдельный продукт"""
    readonly_fields = ['date_added'] # поля только для чтения

    fieldsets = [
        (None,{
                'classes': ['wide'],
                'fields': ['name','quantity','price'],
            },
        ),
        ('Подробности', {
                'description': 'Описание',
                'fields': ['photo','description','date_added'],
            },
        ),        
    ]
    

admin.site.register(Customer, CustomerAdministraion) #
admin.site.register(Product, ProductAdministraion)
admin.site.register(Order)
