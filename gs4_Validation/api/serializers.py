from rest_framework import serializers 
from .models import Student

#---------------------------------Validators-----------------------------------
def starts_with_a(value):
    if value[0].lower() != 'a':
        raise serializers.ValidationError("Name must start with A")
    return value
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[starts_with_a])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data): # instance is the object to be updated
        # print(instance.name) # to print previous name
        instance.name = validated_data.get('name', instance.name) 
        # print(instance.name) # to print updated name
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    #---------------------------------Field Level Validation-----------------------------------
    #This method is automatically invoked when you call .is_valid()
    #Single Field Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value
    
    #---------------------------------Object Level Validation-----------------------------------
    #This method is automatically invoked when you call .is_valid()
    #Multiple Field Validation
    def validate(self, data):
        print(data) #data is a dictionary, which clients sends as a request
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'sundas' and ct.lower() != 'paris':
            raise serializers.ValidationError("City must be paris")
        return data
    
    