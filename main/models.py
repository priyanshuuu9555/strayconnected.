from django.db import models

class StrayReport(models.Model):
    photo = models.ImageField(upload_to='stray_photos/')
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
   # 🆕 Longitude
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report at {self.location} - {self.submitted_at}"
 