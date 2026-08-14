from django.contrib import admin
from django.contrib import admin
from .models import Category, Task
from .models import Category, Task, Bid
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Bid)