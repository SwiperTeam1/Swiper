from lib.sms import send_sms


def submit_phone(request):
    phone = request.POST.get('phone')
    status, msg = send_sms(phone)

    if not status:
        pass



