from .models import Prefectures


def prefectures_list(request):
    prefectures_list = Prefectures.objects.all()

    params = {
        'prefectures_list': prefectures_list,
    }

    return params

