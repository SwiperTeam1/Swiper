from django.db import models

# Create your models here.

class Swiped(models.Model):
    MARK = (
        ('like', 'like'),
        ('dislike', 'dislike'),
        ('superlike', 'superlike')
    )
    uid = models.IntegerField(verbose_name='用户自身id')
    sid = models.IntegerField(verbose_name='被滑的陌生人id')
    mark = models.CharField(choices=MARK, max_length=16, verbose_name='滑动类型')
    time = models.DateTimeField(verbose_name='滑动的时间', auto_now_add=True)
