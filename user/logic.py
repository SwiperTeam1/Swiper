import os

from django.conf import settings

from lib.qiniu import upload_qiniu
from swiper import config
from worker import celery_app

from common import keys


@celery_app.task
def handle_upload(user, avatar):
    filename = keys.AVATAR_KEY % user.id
    filepath = os.path.join(settings.BASE_DIR, settings.MEDIAS, filename)

    with open(filepath, mode='wb') as fp:
        for chunk in avatar.chunks():
            fp.write(chunk)

    upload_qiniu(user, filepath)
    user.avatar = config.QN_URL + filename
    user.save()
