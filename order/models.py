from django.db import models
from purchaser.models import Purchaser
from box.models import Box

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
        
class Brand(models.Model):
    name = models.CharField(max_length=200, default="")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True) 
    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.name
class SizeGladn(models.Model):
    name = models.CharField(max_length=200, default="")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True) 
    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.name
class SizeTerminal(models.Model):
    name = models.CharField(max_length=200, default="")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True) 
    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.name
class TypeTerminal(models.Model):
    name = models.CharField(max_length=200, default="")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True) 
    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.name

class Gladn(models.Model):
    name = models.CharField(max_length=200, default="")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)  
    size = models.ForeignKey(SizeGladn, on_delete=models.CASCADE, null=True, blank=True)  
    type = models.CharField(max_length=200, default="")
    material = models.CharField(max_length=200, default="")
    color = models.CharField(max_length=200, default="" , null=True, blank=True)
    cable0mm123 = models.CharField(max_length=200, default="", null=True, blank=True)
    cable0mm12 = models.CharField(max_length=200, default="" , null=True, blank=True)
    cable0mm1 = models.CharField(max_length=200, default="" , null=True, blank=True)
    af =models.IntegerField(default=0, null=True, blank=True) 
    l =models.IntegerField(default=0, null=True, blank=True) 
    e =models.IntegerField(default=0, null=True, blank=True) 
    wieght =models.IntegerField(default=0, null=True, blank=True) 
    ou =models.IntegerField(default=0, null=True, blank=True) 
    orderNr2070 = models.CharField(max_length=200, default="", null=True, blank=True)
    orderNr5570 = models.CharField(max_length=200, default="", null=True, blank=True)
    price  = models.IntegerField(default=0)    
    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.name
class Terminal(models.Model):
    name = models.CharField(max_length=200, default="")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)  
    size = models.ForeignKey(SizeTerminal, on_delete=models.CASCADE, null=True, blank=True)  
    type = models.ForeignKey(TypeTerminal, on_delete=models.CASCADE, null=True, blank=True)        
    color = models.CharField(max_length=200, default="" , null=True, blank=True)
    material = models.CharField(max_length=200, default="")
    order_No = models.CharField(max_length=200, default="" , null=True, blank=True)
    Width_length_height = models.CharField(max_length=200, default="" , null=True, blank=True)
    current_voltage_UL_A_V = models.CharField(max_length=200, default="" , null=True, blank=True)
    solid_AWG_stranded_AWG_mm2 = models.CharField(max_length=200, default="" , null=True, blank=True)
    stranded_with_ferrule_AWG_mm2 = models.CharField(max_length=200, default="" , null=True, blank=True)
    two_conduct_of_same_type_solid_str_mm2 = models.CharField(max_length=200, default="" , null=True, blank=True)
    cable0mm12 = models.CharField(max_length=200, default="", null=True, blank=True)
    cable0mm1 = models.CharField(max_length=200, default="", null=True, blank=True)
    af =models.IntegerField(default=0, null=True, blank=True) 
    l =models.IntegerField(default=0, null=True, blank=True) 
    e =models.IntegerField(default=0, null=True, blank=True) 
    wieght =models.IntegerField(default=0, null=True, blank=True) 
    ou =models.IntegerField(default=0, null=True, blank=True) 
    orderNr2070 = models.CharField(max_length=200, default="", null=True, blank=True)
    orderNr5570 = models.CharField(max_length=200, default="", null=True, blank=True)
    price  = models.IntegerField(default=0)    
    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.name

    
class Gladns(models.Model):
    name = models.CharField(max_length=200, default="")
    gladn= models.ForeignKey(Gladn, on_delete=models.CASCADE, null=True, blank=True)     
    quantity = models.IntegerField(default=0)  
    position = models.CharField(max_length=10, default="")
    price  = models.IntegerField(default=0)    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)  
    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.name
class Terminals(models.Model):
    name = models.CharField(max_length=200, default="")
    terminal= models.ForeignKey(Terminal, on_delete=models.CASCADE, null=True, blank=True)    
    quantity = models.IntegerField(default=0)   
    position = models.CharField(max_length=10, default="") 
    price  = models.IntegerField(default=0)    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)  
    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.name
class Additional(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=200, null=True, blank=True) 
    options = models.CharField(max_length=200, null=True, blank=True) 
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)  
    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.name

class Component(models.Model):
    name = models.TextField( default="")    
    produkt_terminal= models.ManyToManyField(Terminals,  related_name='terminal_set', blank=True)
    produkt_glands= models.ManyToManyField(Gladns,  related_name='gland_set', blank=True)
    additional_options = models.ManyToManyField(Additional,  related_name='additional_set', blank=True)
    additional_options2 = models.CharField(max_length=200, null=True, blank=True)  
    additional_options3 = models.CharField(max_length=200, null=True, blank=True)  
    price  = models.IntegerField(default=0)    
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True) 
    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, default="")    
    box = models.ForeignKey(Box, on_delete=models.CASCADE, null=True, blank=True)   
    quantity  = models.IntegerField(default=0) 
    price  = models.IntegerField(default=0)     
    component = models.ManyToManyField(Component)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True) 
    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.name
    
# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=200, default="")    
    purchaser = models.ForeignKey(Purchaser, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    price = models.IntegerField(default=0)
    vat = models.IntegerField(default=0)
    coments = models.CharField(max_length=300, null=True, blank=True) 
    title = models.CharField(max_length=200, null=True, blank=True)  
    status_inf = models.CharField(max_length=200, default="",null=True, blank=True)
    status_proc = models.BooleanField( default=False)
    name_name = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField( default=False)  
    is_order = models.BooleanField( default=False)
    is_reservation = models.BooleanField( default=False)
    is_shipment = models.BooleanField( default=False)
    is_staf = models.BooleanField( default=False)
    is_activ = models.BooleanField( default=False)    
    is_available = models.BooleanField( default=False)    
    status_text = models.CharField(max_length=200, null=True, blank=True)      
    category = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    note = models.TextField(max_length=200, null=True, blank=True)
    sys_note = models.TextField(max_length=200, null=True, blank=True)       
    function = models.TextField(null=True, blank=True)    
    conformity = models.CharField(max_length=200, null=True, blank=True)
    info_shotr = models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=200, null=True, blank=True)
    suppliers = models.CharField(max_length=200, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.name