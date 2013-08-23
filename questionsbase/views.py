# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# Create your views here.

def index(request):
	return render_to_response('questionsbase/home.html', context_instance=RequestContext(request))