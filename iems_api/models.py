from django.db.models import (
    Model, ForeignKey, DecimalField, SlugField,
    CharField, IntegerField, CASCADE, Index)

# from django.contrib.gis.db.models import PointField, GeometryCollectionField

class Department(Model):
    department_name = CharField(primary_key=True, max_length=20)
    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        indexes = [
            Index(fields=['department_name'])
        ]
        ordering = ['department_name']

    def __str__(self):
        return self.department_name

class Status(Model):
    status_name = CharField(max_length=20)
    department_name = ForeignKey(
        to=Department, on_delete=CASCADE,
        null=True, blank=True)

    class Meta:
        unique_together = (('department_name', 'status_name'),)
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        indexes = [
            Index(fields=['status_name'])
        ]
        ordering = ['status_name']

    def __str__(self):
        return str(self.department_name) + ": "+self.status_name  

class Enchroachment(Model):
    department_name = ForeignKey(
        to=Department, on_delete=CASCADE,
        null=True, blank=True)   
    status_name = ForeignKey(
        to=Status, on_delete=CASCADE,
        null=True, blank=True)   
    enchrt_id = SlugField(max_length=20, null=True)
    enchrt_type = CharField(max_length=20)
    region = CharField(max_length=20)
    subregion = CharField(max_length=20)
    encrt_size = DecimalField(max_digits=4, decimal_places=2)
    dist_from_center_of_asset = IntegerField()
    criticality = CharField(max_length=6, null=True)
    # centroid = PointField(
    #     srid=4326, null=True, blank=True) 

    class Meta:
        verbose_name = 'Enchroachment'
        verbose_name_plural = 'Enchroachments'
        indexes = [
            Index(fields=['enchrt_id'])
        ]
        ordering = ['enchrt_id']