from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from track import models
import base64

from django.views.generic import ListView
from ipware import get_client_ip


TRACKING_PIXEL = base64.b64decode(
    b"iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
)  # noqa

PNG_MIME_TYPE = "image/png"


def get_request_data(request):
    """Retrieves the user agent and the ip of the client from the Django
    request.

    We use ipware to retrieve the "real" IP (e.g., load balancer will often put
    the client IP in X-Forwarded-For header).
    """
    user_agent = request.META.get("HTTP_USER_AGENT")
    ip = get_client_ip(request)[0]
    return {"user_agent": user_agent, "user_ip": ip}


def index(request):
    pixel = models.TrackPixel.objects.create()
    my_dict = {
        "insert_me": "I am from views.py",
        "img_src": f"http://127.0.0.1:8000/{pixel.pk}/pixel/",
    }
    return render(request, "index.html", context=my_dict)


class OpenTrackingView(View):
    def get(self, request, pixel_id):
        data = get_request_data(request)
        detail = models.TrackDetail.objects.create(**data)
        models.TrackPixel.objects.filter(pk=pixel_id).update(
            is_opened=True, detail=detail
        )
        return HttpResponse(TRACKING_PIXEL, content_type=PNG_MIME_TYPE)


class TrackPixelListView(ListView):
    model = models.TrackPixel
    template_name = "trackpixel_list.html"  # Template file name
    context_object_name = "pixels"  # Context variable name for the template

    def get_queryset(self):
        return super().get_queryset().order_by("-pk")
