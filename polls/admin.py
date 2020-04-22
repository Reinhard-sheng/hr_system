from django.contrib import admin

from . import models

admin.site.register(models.SassUser)
admin.site.register(models.Interviewer)
admin.site.register(models.Message)
admin.site.register(models.InterviewProcess)