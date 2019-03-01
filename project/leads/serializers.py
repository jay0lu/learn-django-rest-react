from rest_framework import serializers
from leads.models import Lead

class LeadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lead
    fields = ('id', 'name', 'email', 'message')  # or use fields = '__all__'
