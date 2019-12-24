import now as now
from django.shortcuts import render

# Create your views here.
from lib.http import render_json
from social.models import Swiped
from user.models import User
import datetime

def get_recd_list(request):
    user = request.user
    now = datetime.datetime.now()
    max_birth_year = now.year - user.profile.min_dating_age
    min_birth_year = now.year - user.profile.max_dating_age

    swiped_list = Swiped.objects.filter(uid=user.id).only('sid')
    sid_list = [s.sid for s in swiped_list]

    sid_list.append(user.id)
    users = User.objects.filter(location=user.profile.location,
                        birth_year__range=[min_birth_year, max_birth_year],
                        sex=user.profile.dating_sex).exclude(id__in=sid_list)
    data = [user.to_dict() for user in users]
    return render_json(data=data)
