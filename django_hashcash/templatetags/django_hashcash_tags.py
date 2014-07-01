# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag()
def hashcashio_public_key():
	'''
	Simply returns the HashCash.IO public key from settings.
	'''
	return settings.HASHCASHIO_PUBLIC_KEY