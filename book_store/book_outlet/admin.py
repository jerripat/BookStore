from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
#Register your models here
admin.site.register(Book, BookAdmin)
