from django.contrib import admin
from .models import House

# Register your models here.

# admin 패널에 House 모델을 연결함
# 아래의 클래스가 House 모델을 통제할거다 라는 뜻의 데코레이터


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ("name", "price_per_night", "address", "pet_allowed")
    list_filter = ("price_per_night", "pet_allowed")
    search_fields = ("address",)
