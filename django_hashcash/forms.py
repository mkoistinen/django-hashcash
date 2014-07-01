# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json
import urllib2
from django import forms
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext as _

class HashCashAuthenticationForm(AuthenticationForm):

    def clean(self):
        '''
        Shims the normal login form to raise validation errors if HashCash.IO
        doesn't provide a proof-of-work.
        '''

        #
        # User didn't toggle the Hashcash.IO switch.
        #
        hashcash_id = self.request.POST.get('hashcashid')
        if not hashcash_id:
            raise forms.ValidationError(_('In order to login, you must first toggle the HasCash.IO switch (<a href="#hashcash-what">what’s this</a>?).'))

        #
        # Fetch the proof of work receipt...
        #
        private_key = settings['HASHCASHIO_PRIVATE_KEY']
        url = 'https://hashcash.io/api/checkwork/{hashcash_id}?apikey={private_key}'.format(
            hashcash_id=hashcash_id,
            private_key=private_key
        )
        response = urllib2.urlopen(url)
        work = json.load(response)

        #
        # Ensure that the work was done.
        #
        if not work or float(work['totalDone']) < 0.01:
            raise forms.ValidationError(_('Please wait for the switch to turn completely green before submitting the form (<a href="#hashcash-why">why</a>?).'))

        #
        # Now, do the normal login
        #
        return super(HashCashAuthenticationForm, self).clean()
