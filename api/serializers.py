from rest_framework import serializers
from base.models import Company, Industry, Technology, SocialMedia, Location, Offer, CompanyIndustry, CompanyTechnology, CompanySocialMedia, CompanyLocation, OfferIndustry, OfferTechnology, OfferLocation, CompanyReport, OfferReport, CompanySuggestion, OfferRequest, AppVersion

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Company
        fields = '__all__'

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Industry
        fields = '__all__'

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Technology
        fields = '__all__'

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = SocialMedia
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Location
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Offer
        fields = '__all__'

class CompanyIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model  = CompanyIndustry
        fields = '__all__'

class CompanyTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model  = CompanyTechnology
        fields = '__all__'

class CompanySocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CompanySocialMedia
        fields = '__all__'

class CompanyLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CompanyLocation
        fields = '__all__'

class OfferIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model  = OfferIndustry
        fields = '__all__'

class OfferTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model  = OfferTechnology
        fields = '__all__'

class OfferLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = OfferLocation
        fields = '__all__'

class CompanyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CompanyReport
        fields = '__all__'

class OfferReportSerializer(serializers.ModelSerializer):
    class Meta:
        model  = OfferReport
        fields = '__all__'


class CompanySuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanySuggestion
        fields = '__all__'

class OfferRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferRequest
        fields = '__all__'

class AppVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppVersion
        fields = '__all__'
