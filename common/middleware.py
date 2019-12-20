from django.utils.deprecation import MiddlewareMixin

from common import errors
from lib.http import render_json
from user.models import User


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        white_list = ['/api/user/submit/phone/',
                      '/api/user/submit/vcode/']
        # print(request.path)
        if request.path in white_list:
            return None

        uid = request.session.get('uid')
        if not uid:
            return render_json(code=errors.LOGIN_REQUIRED, data='请先登录')
        user = User.objects.get(id=uid)
        request.user = user

