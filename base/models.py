from django.db import models

class Company(models.Model):
    name        = models.TextField()
    logo        = models.URLField()
    description = models.TextField()
    address     = models.TextField()
    email       = models.TextField()
    phone       = models.TextField()
    website     = models.URLField()

class Industry(models.Model):
    name = models.TextField()
    logo = models.URLField()
    link = models.URLField()

class Technology(models.Model):
    name = models.TextField()
    logo = models.URLField()
    link = models.URLField()

class SocialMedia(models.Model):
    name = models.TextField()
    logo = models.URLField()
    link = models.URLField()

class Location(models.Model):
    name = models.TextField()
    link = models.URLField()

class Offer(models.Model):
    name        = models.TextField()
    logo        = models.URLField()
    description = models.TextField()
    Type        = models.TextField(choices=[('PFE', 'PFE'), ('Init', 'Init')])
    date        = models.DateField()
    company     = models.ForeignKey(Company, on_delete=models.CASCADE)
    hr_email    = models.TextField()
    hr_phone    = models.TextField()
    apply_link  = models.URLField()

class CompanyIndustry(models.Model):
    company     = models.ForeignKey(Company, on_delete=models.CASCADE)
    industry    = models.ForeignKey(Industry, on_delete=models.CASCADE)

class CompanyTechnology(models.Model):
    company     = models.ForeignKey(Company, on_delete=models.CASCADE)
    technology  = models.ForeignKey(Technology, on_delete=models.CASCADE)

class CompanySocialMedia(models.Model):
    company      = models.ForeignKey(Company, on_delete=models.CASCADE)
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)

class CompanyLocation(models.Model):
    company  = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class OfferIndustry(models.Model):
    offer    = models.ForeignKey(Offer, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

class OfferTechnology(models.Model):
    offer      = models.ForeignKey(Offer, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

class OfferLocation(models.Model):
    offer    = models.ForeignKey(Offer, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class CompanyReport(models.Model):
    company         = models.ForeignKey(Company, on_delete=models.CASCADE)
    user_name       = models.TextField()
    user_company    = models.TextField()
    user_email      = models.TextField()
    user_phone      = models.TextField()
    report_details  = models.TextField()

class OfferReport(models.Model):
    offer           = models.ForeignKey(Offer, on_delete=models.CASCADE)
    user_name       = models.TextField()
    user_company    = models.TextField()
    user_email      = models.TextField()
    user_phone      = models.TextField()
    report_details  = models.TextField()


class CompanySuggestion(models.Model):
    user_name    = models.TextField()
    user_email   = models.TextField()
    user_phone   = models.TextField()
    company_name = models.TextField()
    company_info = models.TextField()

class OfferRequest(models.Model):
    user_name           = models.TextField()
    company_name        = models.TextField()
    user_company_role   = models.TextField()
    user_email          = models.TextField()
    user_phone          = models.TextField()
    offer_title         = models.TextField()
    offer_description   = models.TextField()

class AppVersion(models.Model):
    channel         = models.TextField(choices=[('stable', 'stable'), ('beta', 'beta')])
    current_version = models.TextField()
    link            = models.URLField()
