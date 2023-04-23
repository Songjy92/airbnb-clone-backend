from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words"
    parameter_name = "wordfilter"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, queryset):
        word = self.value()
        if word:
            return queryset.filter(payload__contains=word)
        else:
            return queryset


class RatingFilter(admin.SimpleListFilter):
    title = "Filter by ratings"
    parameter_name = "ratingfilter"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good (greater than 3)"),
            ("bad", "Bad (less than 3)"),
        ]

    def queryset(self, request, queryset):
        print(self.value())
        rating = self.value()
        if rating == "good":
            return queryset.filter(rating__gte=3)
        elif rating == "bad":
            return queryset.filter(rating__lt=3)
        else:
            return queryset


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
        "rating",
    )
    list_filter = (
        "rating",
        "room__category",
        WordFilter,
        RatingFilter,
    )
