from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

now = timezone.now()
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 200)
    quantity = models.PositiveIntegerField()
    description = models.CharField(max_length = 1000, blank=True, null=True)
    created_date = models.DateField(default=now)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name.upper()

class ProductPurchase(models.Model):
    name = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    created_date = models.DateField(default=now)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Products added'

    def __str__(self):
        return self.name.name.upper()

class Requests(models.Model):
    item_name = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    requested_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    requested_date = models.DateField(default=now)
    returnable = models.BooleanField(default=False)
    destination = models.CharField(max_length=300, blank=True, null=True)
    project_name = models.CharField(max_length=300)
    request_status = models.BooleanField(default=False)
    approved_date = models.DateField(null=True, blank=True)
    returned_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Requests'

    def get_approve_url(self):
        return reverse('dashboard:stockRequestsApprove', kwargs={'pk':self.id})

    def get_return_approve_url(self):
        return reverse('dashboard:stockReturn', kwargs={'pk':self.id})

    def __str__(self):
        return self.requested_by.first_name+' '+self.requested_by.last_name+' - '+self.item_name.name.upper()
