from django.db import models

# Create your models here.


class Clients(models.Model):
    username = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=10, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username


class Deposits(models.Model):
    username = models.ForeignKey(Clients, null=True, on_delete=models.SET_NULL)
    mpesa_code = models.CharField(max_length=20, null=True)
    amount = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=15, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username


class Withdrawals(models.Model):
    username = models.ForeignKey(Clients, null=True, on_delete=models.SET_NULL)
    amount = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=15, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username


class Investments(models.Model):
    status = [
        ('pending', 'pending'),
        ('matured', 'matured')
    ]
    username = models.ForeignKey(Clients, null=True, on_delete=models.SET_NULL)
    amount = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=10, null=True, default='pending')
    created = models.DateTimeField(auto_now_add=True, null=True)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.username


class Affiliate(models.Model):
    username = models.ForeignKey(Clients, null=True, on_delete=models.SET_NULL)
    downline = models.CharField(max_length=20, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username
