from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Company, Industry, Technology, SocialMedia, Location, Offer, CompanyIndustry, CompanyTechnology, CompanySocialMedia, CompanyLocation, OfferIndustry, OfferTechnology, OfferLocation, CompanyReport, OfferReport, CompanySuggestion, OfferRequest, AppVersion
from .serializers import CompanySerializer, IndustrySerializer, TechnologySerializer, SocialMediaSerializer, LocationSerializer, OfferSerializer, CompanyIndustrySerializer, CompanyTechnologySerializer, CompanySocialMediaSerializer, CompanyLocationSerializer, OfferIndustrySerializer, OfferTechnologySerializer, OfferLocationSerializer, CompanyReportSerializer, OfferReportSerializer, CompanySuggestionSerializer, OfferRequestSerializer, AppVersionSerializer


@api_view(['GET'])
def companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies,many=True)

    data = serializer.data

    for item in data:
        companyLoc = CompanyLocation.objects.filter(company=item['id'])
        companyInd = CompanyIndustry.objects.filter(company=item['id'])
        listLoc = []
        listInd = []
        for item2 in companyLoc:
            listLoc.append(item2.location.id)
        for item2 in companyInd:
            listInd.append(item2.Industry.id)
        item['location_id_list'] = listLoc
        item['industry_id_list'] = listInd
        item.pop('description', None)
        item.pop('address', None)
        item.pop('email', None)
        item.pop('phone', None)
        item.pop('website', None)

    return Response(data)

@api_view(['POST'])
def addCompany(request):
    serializer = CompanySuggestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("200 ok")
    print(serializer.errors)
    return Response("400 bad request")

@api_view(['GET'])
def offers(request):
    offer = Offer.objects.all()
    serializer = OfferSerializer(offer,many=True)

    data = serializer.data

    for item in data :
        companyLoc = CompanyLocation.objects.filter(company=item['company'])
        companyInd = CompanyIndustry.objects.filter(company=item['company'])
        companyTech = CompanyTechnology.objects.filter(company=item['company'])
        listLoc = []
        listInd = []
        listTech = []
        for item2 in companyLoc:
            listLoc.append(item2.location.id)
        for item2 in companyInd:
            listInd.append(item2.Industry.id)
        for item2 in companyTech:
            listTech.append(item2.Technology.id)
        item['location_id_list'] = listLoc
        item['industry_id_list'] = listInd
        item['technology_id_list'] = listTech
        item.pop('description', None)
        item.pop('hr_email', None)
        item.pop('hr_phone', None)
        item.pop('apply_link', None)

    return Response(data)


@api_view(['GET'])
def industries(request):
    industries = Industry.objects.all()
    serializer = IndustrySerializer(industries, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def technologies(request):
    technologies = Technology.objects.all()
    serializer = TechnologySerializer(technologies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def socialmedias(request):
    socialmedias = SocialMedia.objects.all()
    serializer = SocialMediaSerializer(socialmedias, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def locations(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def version(request, channel):
    try:
        app_version = AppVersion.objects.get(channel=channel)
        data = {
            'current_version': app_version.current_version,
            'link': app_version.link
        }
        return Response(data, status=200)
    except AppVersion.DoesNotExist:
        return Response("400 bad request", status=400)

@api_view(['GET'])
def company(request, id):
    try:
        company = Company.objects.get(id=id)
        data = {
            'id': company.id,
            'name': company.name,
            'logo': company.logo,
            'description': company.description,
            'address': company.address,
            'email': company.email,
            'phone': company.phone,
            'website': company.website,
            'industry_id_list': list(company.companyindustry_set.values_list('industry_id', flat=True)),
            'location_id_list': list(company.companylocation_set.values_list('location_id', flat=True)),
            'technology_id_list': list(company.companytechnology_set.values_list('technology_id', flat=True)),
            'socialmedia_id_list': list(company.companysocialmedia_set.values_list('socialmedia_id', flat=True))
        }
        return Response(data, status=200)
    except Company.DoesNotExist:
        return Response("400 bad request", status=400)


@api_view(['GET', 'POST'])
def offer(request, id=None):
    if request.method == 'GET':
        try:
            offer = Offer.objects.get(id=id)
            data = {
                'id': offer.id,
                'name': offer.name,
                'logo': offer.logo,
                'description': offer.description,
                'type': offer.Type,
                'date': offer.date.isoformat(),
                'company_id': offer.company_id,
                'hr_email': offer.hr_email,
                'hr_phone': offer.hr_phone,
                'apply_link': offer.apply_link,
                'industry_id_list': list(offer.offerindustry_set.values_list('industry_id', flat=True)),
                'location_id_list': list(offer.offerlocation_set.values_list('location_id', flat=True)),
                'technology_id_list': list(offer.offertechnology_set.values_list('technology_id', flat=True))
            }
            return Response(data, status=200)
        except Offer.DoesNotExist:
            return Response("400 bad request", status=400)
    elif request.method == 'POST':
        serializer = OfferRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("200 OK", status=200)
        else:
            return Response("400 bad request", status=400)


@api_view(['POST'])
def report_offer(request):
    serializer = OfferReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("200 OK", status=200)
    else:
        return Response("400 bad request", status=400)

@api_view(['POST'])
def report_company(request):
    serializer = CompanyReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("200 OK", status=200)
    else:
        return Response("400 bad request", status=400)
