# shop/context_processors.py


def media_url(request):
    from django.conf import settings

    return {"MEDIA_URL": settings.MEDIA_URL}
