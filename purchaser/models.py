from django.db import models

# Create your models here.


class Purchaser(models.Model):
    name = models.CharField(max_length=200, default="")
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")
    position = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    company_adress = models.CharField(max_length=200, null=True, blank=True)
    company_zip_code = models.CharField(max_length=200, null=True, blank=True)
    company_city = models.CharField(max_length=200, null=True, blank=True)
    company_country = models.CharField(max_length=200, null=True, blank=True)
    person_name = models.CharField(max_length=200, null=True, blank=True)
    person_adress = models.CharField(max_length=200, null=True, blank=True)
    person_zip_code = models.CharField(max_length=200, null=True, blank=True)
    person_city = models.CharField(max_length=200, null=True, blank=True)
    person_country = models.CharField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(default=0)
    nip = models.IntegerField(default=0)
    vat = models.IntegerField(default=0)
    name_name = models.CharField(max_length=200, null=True, blank=True)
    is_staf = models.BooleanField( default=False)
    is_activ = models.BooleanField( default=False)
    rodo = models.BooleanField( default=False)
    status_text = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField( default=False)
    title = models.CharField(max_length=200, null=True, blank=True)    
    weight = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    note = models.TextField(max_length=200, null=True, blank=True)
    sys_note = models.TextField(max_length=200, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)    
    function = models.TextField(null=True, blank=True)    
    conformity = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.name
