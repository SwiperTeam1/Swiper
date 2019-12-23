from qiniu import Auth, put_file, etag

from common import keys
from swiper import config


def upload_qiniu(user, file_path):
    q = Auth(config.QN_AK, config.QN_SK)

    bucket_name = 'sz1906'
    filename = keys.AVATAR_KEY % user.id

    token = q.upload_token(bucket_name, filename, 3600)
    ret, info = put_file(token, filename, file_path)
    print(info)
    print(ret)
