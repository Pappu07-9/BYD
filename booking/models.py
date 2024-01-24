from asyncio.windows_events import NULL
from django.db import models
from django.forms import NullBooleanField
from sales.models import Masterdata
# Create your models here.
class Booking(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True,auto_created=True,null=False)
    usertracker = models.CharField(default= "null", max_length=30)
    name_of_customer = models.CharField(max_length=200, default='name')
    address_of_customer = models.CharField(max_length=200, default='address')
    number_of_customer = models.IntegerField(blank=True)
    reference = models.TextField('write a reference')
    interested_model = models.CharField(
        max_length=200,
        choices=[
        ('atto 3 advanced', 'Atto 3 Advanced'),
        ('atto 3 superior', 'Atto 3 Superior'),
        ('atto 3 premium', 'Atto 3 Premium'),
        ('dolphin', 'Dolphin'),
        ('e6', 'E6'),
        ('m3', 'M3'),
        ('seal', 'Seal'),
        ],
        )
    lead_by = models.CharField(default='none',
            max_length=200,
            choices=[
            ('generated', 'Generated'),
            ('walk in', 'walk in'),
            ],
            )
#     follow_update = models.DateField(str("%YYYY-DD_MM%"))
    status = models.CharField(default='warm',
            max_length=200,
            choices=[
            ('hot', 'Hot'),
            ('cold', 'Cold'),
            ('warm', 'Warm'),
            ],
            )
    book_status = models.BooleanField(default=False)
    test_drive = models.BooleanField(default=False)
    etd = models.CharField(default=None, max_length=100)
