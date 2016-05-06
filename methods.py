# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.conf import settings
from .models import Application, Crash
import xml.etree.ElementTree as ET
import re, base64
import logging

def parse_useragent(useragent):
    return re.findall(r'(\w[\s\w]*)/(\d+)', useragent)

def get_authentication(request):
    if not 'HTTP_AUTHORIZATION' in request.META:
        raise PermissionDenied

    auth = request.META['HTTP_AUTHORIZATION'].split()
    if not auth or not len(auth) == 2:
        raise PermissionDenied

    if auth[0].lower() != "basic":
        raise PermissionDenied

    username, password = base64.b64decode(auth[1]).split(':')
    if not username or not password or username != password:
        raise PermissionDenied

    return password

def get_application(request):
    if not 'HTTP_USER_AGENT' in request.META:
        raise PermissionDenied

    useragent = parse_useragent(request.META['HTTP_USER_AGENT'])
    if not useragent or not len(useragent) >= 1:
        raise PermissionDenied

    program = useragent[0]
    if not program or not len(program) == 2:
        raise PermissionDenied

    application = get_object_or_404(Application, name=program[0])
    build = int(program[1])
    return application, build

def create_response(request):
    response = HttpResponse('Crash report successfully send, thanks!', content_type='text/plain', status=201)
    response['Status'] = 201
    return response

@csrf_exempt
def post_crashreport(request):
    if request.method != 'POST':
        raise Http404

    application, build = get_application(request)
    if not application or not build:
        raise Http404

    report = ('\n'.join(request.readlines())).strip()
    if not report or len(report) > 1024:
        raise Http404

    Crash.objects.create(application=application,
                         build=build,
                         report=report,
                         is_obsolete=True)

    return create_response(request)

@csrf_exempt
def post_issue(request):
    if request.method != 'POST':
        raise Http404

    application, build = get_application(request)
    if not application or not build:
        raise Http404

    key = get_authentication(request)
    if not key or key != settings.BUGS_POST_ISSUE_KEY:
        raise PermissionDenied

    try:
        parser = ET.XMLParser(encoding='utf-8')
        issue = ET.fromstring(request.body, parser=parser)
    except Exception, e:
        logging.exception(e)
        e1 = RuntimeError(request)
        logging.exception(e1)
        e2 = RuntimeError(request.body)
        logging.exception(e2)
        raise e
    if issue is None:
        raise Http404

    project_id = issue.find('project_id').text
    subject = issue.find('subject').text
    description = issue.find('description').text

    if not project_id or int(project_id) != settings.BUGS_POST_ISSUE_PID:
        raise Http404

    if not subject or not description:
        raise Http404

    report = description.strip()
    if not report:
        raise Http404

    if not report or len(report) > 1024:
        raise Http404

    Crash.objects.create(application=application,
                         build=build,
                         report=report)

    return create_response(request)
