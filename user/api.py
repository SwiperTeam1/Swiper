from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from lib.http import render_json
from lib.sms import send_sms
from common import errors, keys
from user.models import User


def submit_phone(request):
    phone = request.POST.get('phone')
    status, msg = send_sms(phone)
    if not status:
        # return JsonResponse({'code': errors.SMS_ERROR, 'data': '短信发送失败'})
        return render_json(code=errors.SMS_ERROR, data='短信发送失败')
    # return JsonResponse({'code': 0, 'data': None})
    return render_json()


def submit_vcode(request):
    phone = request.POST.get('phone')
    vcode = request.POST.get('vcode')

    cached_vcode = cache.get(keys.VCODE_KEY % phone)
    if vcode == cached_vcode:
        # try:
        #     user = User.objects.get(phonenum=phone)
        # except User.DoesNotExist:
        #     user = User.objects.create(phonenum=phone, nickname=phone)
        user, _ = User.objects.get_or_create(phonenum=phone, defaults={'nickname': phone})
        request.session['uid'] = user.id
        return render_json(data=user.to_dict())
    else:
        return render_json(code=errors.VCODE_ERROR, data='验证码错误')

def get_profile(request):
    uid = request.session.get('uid')
    if not uid:
        return render_json(code=errors.LOGIN_REQUIRED, data="请登录")
    user = User.objects.get(id=uid)
    return render_json(data=user.profile.to_dict())

