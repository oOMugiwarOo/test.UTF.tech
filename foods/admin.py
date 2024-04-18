from django.contrib import admin

from .models import Food, FoodCategory


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "name_en", "name_ch", "order_id")
    search_fields = ("name_ru", "name_en", "name_ch", "order_id")
    list_filter = ("name_ru", "name_en", "name_ch", "order_id")


class FoodAdmin(admin.ModelAdmin):
    list_display = (
        "name_ru",
        "is_publish",
        "category",
        "is_vegan",
        "is_special",
        "code",
        "internal_code",
        "description_ru",
        "description_en",
        "description_ch",
        "cost",
    )
    search_fields = (
        "name_ru",
        "is_publish",
        "category",
        "is_vegan",
        "is_special",
        "code",
        "internal_code",
        "description_ru",
        "description_en",
        "description_ch",
        "cost",
    )
    list_filter = ("category", "is_vegan")


admin.site.register(Food, FoodAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)
