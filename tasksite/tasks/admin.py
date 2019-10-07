from django.contrib import admin
from tasks.models import Question, Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)


admin.site.site_header = 'سیستم مدیریت وظایف'