from django.contrib import admin
from .models import Products,Order

# Register your models here.
admin.site.site_header='E-Commerce site'
admin.site.site_title='ABC Shopping'
admin.site.index_title='Manage ABC Shopping'
admin.site.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display=('title','price','category','discounted_price','image','description')
    search_fields=('title','category','description',)
    def change_category_to_default(self,request,queryset):
        queryset.update(category='default')
    change_category_to_default.short_description='Default Category'
    actions=('change_category_to_default',)
    list_editable=('price','category')

admin.site.register(Products,ProductAdmin)