## @package serializers
#    Contains serializer classes for the \ref models module

from rest_framework import serializers
from models import Car


class CarSerializer(serializers.ModelSerializer):
    ## The serializer for the \ref Car model.
    # serializes all the fields of the Car model. \see Car
    # The JSON schema that this class returns is
    #{'id':<db entry id>,
    #  'created':<datetime of object creation>  ,
    #  'vin':<the car vin number>,
    #  'make':<make of car>,
    #  'model':<model of car>
    #}
    class Meta:
        model = Car
        fields = ('id', 'created', 'vin', 'make', 'carmodel', )

