from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site

import httplib2
from oauth2client.django_orm import Storage
from apiclient.discovery import build

from pickipicki.apps.metrics.models import CredentialsModel

class Analytics(models.Model):
    site = models.ForeignKey(Site)
    analytics_code = models.CharField(blank=True, max_length=100)
    profile_id = models.CharField(blank=True, null=True, max_length=100)
    
    
    def getProfileId(self, user):
        
        storage = Storage(CredentialsModel, 'id', user, 'credential')
        credential = storage.get()
        
        if credential is not None:
            http = httplib2.Http()
            http = credential.authorize(http)
    
            service = build("analytics", "v3", http=http)
            
            accounts = service.management().accounts().list().execute()
    
            if accounts.get('items'):
                # Get the first Google Analytics account
    
                for account in accounts.get('items'):
                    accountId = account.get('id')
    
                    # Get a list of all the Web Properties for the first account
                    code = self.analytics_code
    
                    try:
                        webproperty = service.management().webproperties().get(accountId=accountId,webPropertyId=code).execute()
    
                        if webproperty.get('id'):
                            # Get the first Web Property ID
                            firstWebpropertyId = webproperty.get('id')
    
                            # Get a list of all Views (Profiles) for the first Web Property of the first Account
                            profiles = service.management().profiles().list(
                                accountId=accountId,
                                webPropertyId=firstWebpropertyId).execute()
    
                            if profiles.get('items'):
                                # return the first View (Profile) ID
                                self.profile_id =  profiles.get('items')[0].get('id')
                                self.save()
                    except HttpError:
                        #web property not part of found accountId
                        pass
            

    def __unicode__(self):
        return u"%s" % (self.analytics_code)
    
    class Meta:
        verbose_name_plural = "Analytics"
