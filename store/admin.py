from django.contrib import admin
from store.models import ProductModel, CategoryModel, BestProductModel, AdsModel, HotOfferModel
# Register your models here.


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_publish']
    list_filter = ['price', 'is_publish']
    search_fields = ['name']


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class BestProductModelAdmin(admin.ModelAdmin):
    list_display = ['product']
    search_fields = ['product']


class AdsModelAmin(admin.ModelAdmin):
    list_display = ['text', 'is_publish']


class HotOfferModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'discount', 'new_price', 'time', 'is_publish']


admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(BestProductModel, BestProductModelAdmin)
admin.site.register(AdsModel, AdsModelAmin)
admin.site.register(HotOfferModel, HotOfferModelAdmin)
