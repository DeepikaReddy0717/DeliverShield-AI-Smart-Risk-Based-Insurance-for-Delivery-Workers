from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Worker, InsurancePlan, Claim

admin.site.register(Worker)
admin.site.register(InsurancePlan)
admin.site.register(Claim)