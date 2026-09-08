from django.contrib import admin
from .models import Houses, Users

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=("user_id","username","real_name","phone","email",
                  "role","id_card","gender","status")
    search_fields=("username","phone")
    list_filter=("role","status","gender")
    list_per_page=50
admin.site.register(Users,UserAdmin)

class HousesAdmin(admin.ModelAdmin):
    list_display=("house_id","owner_id__username","title","address",
                  "business_area","house_type","layout","area_sqm",
                  "orientation","floor_info","decoration","monthly_rent","deposit","status")
    
    search_fields=("title","address")
    list_filter=("status","floor_info")
    list_per_page=50
admin.site.register(Houses,HousesAdmin)