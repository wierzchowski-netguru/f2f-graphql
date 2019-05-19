from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from core.models import Forum, Post, Thread

User = get_user_model()


@admin.decorators.register(Forum)
class ForumAdmin(ModelAdmin):

    class Meta:
        model = Forum


@admin.decorators.register(Thread)
class ThreadAdmin(ModelAdmin):
    list_display = ['id', 'name', 'user']

    class Meta:
        model = Thread


@admin.decorators.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['id', 'text', 'user']

    class Meta:
        model = Post


@admin.decorators.register(User)
class UserAdmin(UserAdmin):
    pass
