from django.views.decorators.csrf import csrf_exempt
from sms.shiting import *

@csrf_exempt
def webhook(request):
    webhook_secret = 'WebhookSecret'
    req = request.POST

    if len(req)==1:
        req = list(dict(req))[0]
        req = [element.split(':') for element in req.split(', ')]
        req = dict([element[0],element[1]] for element in req)

    if req.get('secret') != webhook_secret:
        return HttpResponse(":)", 'text/plain', 403)

    if req.get('event') in 'incoming_message':
        content = req.get('content').split('$')
        result = keyword(content[0],content[1:])
        return result
