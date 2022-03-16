from django.db import models
import uuid

# Create your BOX models here.


class Box(models.Model):
    name = models.CharField(max_length=200, default="")
    code = models.CharField(max_length=200,default="")
    max_hubs_side_a_b = models.ForeignKey(
        'MaxHubsSideAB', on_delete=models.CASCADE, null=True, blank=True)
    max_hubs_side_c_d = models.ForeignKey(
        'MaxHubsSideCD', on_delete=models.CASCADE, null=True, blank=True)
    termina = models.ForeignKey(
        'Termina', on_delete=models.CASCADE, null=True, blank=True)
    overall_dimension_d = models.IntegerField(default=0)
    overall_dimension_w = models.IntegerField(default=0)
    overall_dimension_h = models.IntegerField(default=0)
    internal_dimension_a = models.IntegerField(default=0)
    internal_dimension_b = models.IntegerField(default=0)
    internal_dimension_c = models.IntegerField(default=0)
    mounting_plate_d = models.IntegerField(default=0)
    mounting_plate_e = models.IntegerField(default=0)
    fixing_dimension_f = models.IntegerField(default=0)
    fixing_dimensions_g = models.IntegerField(default=0)
    fixing_dimensions_screw = models.CharField(max_length=10, default="M 4/6")
    title = models.CharField(max_length=200, null=True, blank=True)
    certificate = models.ForeignKey(
        'Certificate', on_delete=models.CASCADE, null=True, blank=True)
    maximum_power_dissipation = models.ForeignKey(
        'MaximumPowerDissipation', on_delete=models.CASCADE, null=True, blank=True)
    weight = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    ambient_temperature = models.CharField(
        max_length=200,  default="–40°C +60°C")
    degree_of_protection = models.CharField(
        max_length=200,  default="IP66", null=True, blank=True)
    class_of_protection = models.CharField(
        max_length=200,  default="II", null=True, blank=True)
    temperature_class = models.CharField(
        max_length=200,  default="T6/T5/T4", null=True, blank=True)
    maximum_voltage = models.CharField(
        max_length=200,  default="1100 V", null=True, blank=True)
    maximum_current = models.CharField(
        max_length=200,  default="234 A", null=True, blank=True)
    mechanical_riskn = models.CharField(
        max_length=200,  default="7 J", null=True, blank=True)
    color = models.CharField(
        max_length=200,  default="Black", null=True, blank=True)
    type_of_protection = models.CharField(
        max_length=200,  default="Ex-e", null=True, blank=True)
    material = models.CharField(
        max_length=200,  default="Glass fiber reinforced polyester resin", null=True, blank=True)
    marking_gb_terminal_boxes = models.CharField(max_length=200,
                                                 default="II 2GD Ex e ia IIC T6/T5 Gb")
    marking_db_terminal_boxes = models.CharField(max_length=200,
                                                 default="Ex tb IIIC T85/T100°C Db")
    marking_gb_terminal_control_stations = models.CharField(max_length=200,
                                                            default="II 2GD Ex d e [ia/ib] mb IIC T6/T5/T4 Gb")
    marking_db_terminal_control_stations = models.CharField(max_length=200,
                                                            default="Ex tb IIIC T85/T100/T135°C Db")
    marking_db_terminal_control_stations = models.CharField(max_length=200,
                                                            default="Ex tb IIIC T85/T100/T135°C Db")
    description = models.TextField(null=True, blank=True)
    note = models.TextField(max_length=200, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    description_function = models.TextField(null=True, blank=True)
    description_constructin = models.TextField(null=True, blank=True)
    description_accessories = models.TextField(null=True, blank=True)
    description_protection = models.TextField(null=True, blank=True)
    conformity = models.CharField(max_length=200, null=True, blank=True)
    protection_category = models.CharField(
        max_length=200, default="suitable for Zone 1- 2 (gas) and Zone 21 - 22 (dust)", null=True, blank=True)
    completed = models.BooleanField(default=False)
    option = models.JSONField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.code

    class Meta:
        unique_together = ['max_hubs_side_a_b', 'max_hubs_side_c_d']

# class Album(models.Model):

class Certificate(models.Model):
    code = models.CharField(max_length=200)
    certificate_number = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.code


class MaximumPowerDissipation(models.Model):
    code = models.CharField(max_length=200)
    certificate_number = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.code


class MaxHubsSideAB(models.Model):
    code = models.CharField(max_length=200)
    m12 = models.IntegerField(default=0)
    m16 = models.IntegerField(default=0)
    m20 = models.IntegerField(default=0)
    m25 = models.IntegerField(default=0)
    m32 = models.IntegerField(default=0)
    m40 = models.IntegerField(default=0)
    m50 = models.IntegerField(default=0)
    m60 = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.code
# class Track(models.Model):

class MaxHubsSideCD(models.Model):
    code = models.CharField(max_length=200)
    m12 = models.IntegerField(default=0)
    m16 = models.IntegerField(default=0)
    m20 = models.IntegerField(default=0)
    m25 = models.IntegerField(default=0)
    m32 = models.IntegerField(default=0)
    m40 = models.IntegerField(default=0)
    m50 = models.IntegerField(default=0)
    m60 = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.code


class Termina(models.Model):
    code = models.CharField(max_length=200)
    t15 = models.IntegerField(default=0)
    t25 = models.IntegerField(default=0)
    t40 = models.IntegerField(default=0)
    t60 = models.IntegerField(default=0)
    t100 = models.IntegerField(default=0)
    t160 = models.IntegerField(default=0)
    t350 = models.IntegerField(default=0)
    t500 = models.IntegerField(default=0)
    t700 = models.IntegerField(default=0)
    t950 = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.code


class Order(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    panels = models.JSONField(null=True, blank=True)
    code = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    note = models.TextField(max_length=200, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    conformity = models.BooleanField(max_length=200, null=True, blank=True)
    completed = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        # ustawia title w panelu damina jaki podajemy w title
        return self.email
