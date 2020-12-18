from django.contrib import admin
from .models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated") # aparece na tela essas informações
    prepopulated_fields = {"slug":("title",)} # preenche automaticamente o slug a partir do titulo
