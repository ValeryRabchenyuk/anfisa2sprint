from django.contrib import admin


from .models import Category, IceCream, Topping, Wrapper


# Register your models here.
# Из модуля models импортируем модель Category
from .models import Category
from .models import Topping
from .models import Wrapper
from .models import IceCream


empty_value_display = 'Не задано'


# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )    
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)


# Регистрируем класс с настройками админки для моделей IceCream и Category:

admin.site.register(Category, CategoryAdmin)
admin.site.register(IceCream, IceCreamAdmin)

# Регистрируем модели Topping и Wrapper, 
# чтобы ими можно было управлять через админку
# (интерфейс админки для этих моделей останется стандартным):
admin.site.register(Topping)
admin.site.register(Wrapper)


filter_horizontal = ('toppings',)
