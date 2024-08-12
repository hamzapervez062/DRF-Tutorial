from rest_framework import serializers
from .models import Student

# ModelSerializer class provies a shortcut that lets you create a serializer class automatically with fields that correspond to the model's fields.
# it will automatically generate a set of fields that match the model's fields, and validators.
# it includes simple default implementations of create() and update() methods.

 # Validators
# def starts_with_a(value):
#     if value[0].lower() != 'a':
#         raise serializers.ValidationError("Name must start with a")
#     return value

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    # name = serializers.CharField(validators=[starts_with_a])
    
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['name'] # it will not allow to update the name field.

        # extra_kwargs = {
        #     'name': {'read_only': True},
        # }

    # Field level validation
    # def validate_roll(self, value):
    #         if value >= 200:
    #             raise serializers.ValidationError("Seat Full")
    #         return value
        
    # # Object level validation
    # def validate(self, data):
    #         nm = data.get('name')
    #         ct = data.get('city')
    #         if nm.lower() == 'mohsin' and ct.lower() != 'lahore':
    #             raise serializers.ValidationError("City must be lahore")
    #         return data
        
   