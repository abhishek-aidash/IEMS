from rest_framework.serializers import (
    CharField, IntegerField,
    DecimalField, Serializer)

# from rest_framework_gis.serializers import GeometryField    

class DepartmentSerializer(Serializer):
    department_name = CharField()   

class StatusResSerializer(Serializer):
    status_name = CharField()
    department_name = CharField()

class EnchroachmentSerializer(Serializer):  
    department_name = CharField(default=None) 
    status_name = CharField(default=None) 
    enchrt_id = CharField(default=None)
    enchrt_type = CharField(default=None)
    region = CharField(default=None)
    subregion = CharField(default=None)
    encrt_size = DecimalField(max_digits=10, decimal_places=2, default=None)
    dist_from_center_of_asset = IntegerField()
    criticality = CharField(default=None)
    # centroid = GeometryField(allow_null=True)
