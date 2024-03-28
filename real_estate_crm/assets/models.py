from django.db import models

class Employee(models.Model):
    id_no = models.CharField(max_length=100,null=True, unique=False)
    department = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=100,null=True)
    habesha_name = models.CharField(max_length=50,null=True)
    subcity = models.CharField(max_length=50,null=True)
    woreda = models.CharField(max_length=15,null=True)
    house_num = models.CharField(max_length=50,null=True)
    phone_number = models.CharField(max_length=50,null=True)
    sim_type = models.CharField(max_length=50,null=True)
    photo_number = models.CharField(max_length=50,null=True)
    last_id_no = models.CharField(max_length=50,null=True)
    
    

    def __str__(self):
        return self.name

class Asset(models.Model):
    ITEM_TYPES = [
        ('Laptop', 'Laptop'),
        ('Desktop', 'Desktop'),
        ('Access Card', 'Lift Access Card'),
        ('Printer', 'Printer'),
        ('Connector', 'Connector'),
    ]
    item_type = models.CharField(max_length=50, choices=ITEM_TYPES)
    item_model = models.CharField(max_length=100)
    taken_date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.item_type} - {self.item_model} assigned to {self.employee}"
