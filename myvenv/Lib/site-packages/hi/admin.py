from django.contrib import admin
from .models import Blog, Choice, Question,Pictures
# Register your models here.


admin.site.register(Blog)
admin.site.register(Choice)
admin.site.register(Question)

admin.site.register(Pictures)