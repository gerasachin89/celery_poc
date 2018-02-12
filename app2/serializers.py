from rest_framework import serializers
from app2.models import Bike, Person, detail

class BikeSerializer(serializers.ModelSerializer):
    COLOR_OPTIONS = ('yellow', 'black')

    color = serializers.ChoiceField(choices=COLOR_OPTIONS)
    size = serializers.FloatField(min_value=30.0, max_value=60.0)
    #model = serializers.CharField(max_length=None, min_length=None, allow_blank=False)

    class Meta:
        model = Bike
        fields = ['color', 'size']

class detailSerializer(serializers.ModelSerializer):

    class Meta:
        model = detail
        fields=('id','person', 'detail')

class upcellacceptSerializer(serializers.ModelSerializer):
    det = detailSerializer()
    #det = serializers.PrimaryKeyRelatedField(read_only=True)
    #det = serializers.SlugRelatedField(queryset=detail.objects.all(), slug_field='detail')
    #det = serializers.SlugRelatedField(queryset=detail.objects.all(), slug_field='id')
    class Meta:
        model = Person
        fields=('id','first_name', 'det')
        #fields = '__all__'
