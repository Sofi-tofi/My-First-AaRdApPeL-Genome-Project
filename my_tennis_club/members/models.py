from django.db import models

# Create your models here.

class Member(models.Model):
  run = models.CharField(max_length=255)
  bioproject = models.CharField(max_length=255)
  biosample = models.CharField(max_length=255)
  assay_type = models.CharField(max_length=255)
  center_name = models.CharField(max_length=255)
  experiment = models.CharField(max_length=255)
  instrument = models.CharField(max_length=255)
  library_layout = models.CharField(max_length=255)
  library_selection = models.CharField(max_length=255)
  library_source = models.CharField(max_length=255)
  org = models.CharField(max_length=255)
