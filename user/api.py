from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from lib.http import render_json
from lib.sms import send_sms
from common import errors


def submit_phone(request):
    phone = request.POST.get('phone')
    status, msg = send_sms(phone)
    if not status:
        # return JsonResponse({'code': errors.SMS_ERROR, 'data': '短信发送失败'})
        return render_json(code=errors.SMS_ERROR, data='短信发送失败')
    # return JsonResponse({'code': 0, 'data': None})
    return render_json()
