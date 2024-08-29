from django.db import models


class TrackDetail(models.Model):
    user_agent = models.CharField(max_length=255)
    user_ip = models.CharField(max_length=255)


class TrackPixel(models.Model):
    is_opened = models.BooleanField(default=False)
    detail = models.ForeignKey(TrackDetail, null=True, on_delete=models.CASCADE)
