from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Type(models.Model):
    
    name = models.CharField(max_length=125)    

    class Meta:
        verbose_name = _("Type")
        verbose_name_plural = _("Types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Type_detail", kwargs={"pk": self.pk})

class Product(models.Model):

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    type = ForeignKey(Type, on_delete=models.CASCADE, related_name='product_type')
    user = ForeignKey(User, on_delete=models.CASCADE, related_name='product_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})
