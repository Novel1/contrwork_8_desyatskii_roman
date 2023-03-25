from django.contrib import admin

from webapp.models import Product, Review


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'image', 'created_at')
    list_filter = ('id', 'name', 'description', 'category', 'created_at')
    search_fields = ('name', 'description', 'category')
    fields = ('name', 'description', 'image', 'category', 'created_at')
    readonly_fields = ('id', 'created_at')


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'grade', 'product', 'created_at')
    list_filter = ('id', 'author', 'text', 'grade', 'product', 'created_at')
    search_fields = ('author', 'text', 'grade', 'product')
    fields = ('author', 'text', 'product', 'grade', 'created_at')
    readonly_fields = ('id', 'created_at')


admin.site.register(Review, ReviewAdmin)
