from django import forms
from .models import Worker, InsurancePlan


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'city', 'platform', 'daily_income', 'plan']


class InsurancePlanForm(forms.ModelForm):
    class Meta:
        model = InsurancePlan
        fields = ['name', 'weekly_premium', 'coverage']