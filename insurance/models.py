from django.db import models

# Create your models here.
from django.db import models
class Worker(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    daily_income = models.IntegerField()

    plan = models.ForeignKey(
        "InsurancePlan",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class InsurancePlan(models.Model):
    PLAN_TYPES = [
        ("Basic", "Basic"),
        ("Standard", "Standard"),
        ("Premium", "Premium"),
    ]

    name = models.CharField(max_length=20, choices=PLAN_TYPES)
    weekly_premium = models.IntegerField()
    coverage = models.TextField()

    def __str__(self):
        return self.name


class Claim(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    disruption_reason = models.CharField(max_length=200)
    payout_amount = models.IntegerField()
    status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return f"{self.worker.name} - {self.disruption_reason}"