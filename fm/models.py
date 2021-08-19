from django.db import models

# Create your models here.
class Motor(models.Model):
    oem = models.CharField(("OEM"), max_length=50)
    qty = models.IntegerField(("QTY"))
    hp = models.DecimalField(("HP"), max_digits=7, decimal_places=2)
    
    class Meta:
        verbose_name = ("motor")
        verbose_name_plural = ("motors")

    def __str__(self):
        return self.oem

    def get_absolute_url(self):
        return reverse("motor_detail", kwargs={"pk": self.pk})

