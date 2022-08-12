from django.contrib import admin
from .models import Task, User,Project,Comment, Priority
# Register your models here.
admin.site.register(User),
admin.site.register(Project),
admin.site.register(Comment),
admin.site.register(Task),
admin.site.register(Priority)