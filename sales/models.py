from django.conf import settings
import random
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import datetime,date

User = get_user_model()

# Create your models here.
class Masterdata(models.Model):
    Id = models.AutoField(auto_created=True, primary_key=True ,null= False)
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
    follow_update = models.DateField(auto_now=False,auto_now_add=False, blank=True)
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

# def get_random_masterdata(request):
#     if not _random_masterdata_set: # initialize the set if it's empty
#         _random_masterdata_set = set(Masterdata.objects.values_list('id', flat=True))

#     # generate a random id from the ids in the set
#     random_id = random.choice(list(_random_masterdata_set))

#     # remove the random id from the set to avoid repetition
#     _random_masterdata_set.remove(random_id)

#     # get the master data object with the random id
#     random_masterdata = Masterdata.objects.get(id=random_id)

#     return random_masterdata
_random_masterdata_set = []

def get_random_masterdata():
    global _random_masterdata_set

    if not _random_masterdata_set: # initialize the set if it's empty
        _random_masterdata_set = set(Masterdata.objects.values_list('Id', flat=True))

    # generate a random id from the ids in the set
    random_id = random.choice(list(_random_masterdata_set))

    # remove the random id from the set to avoid repetition
    _random_masterdata_set.remove(random_id)

    # get the master data object with the random id
    random_masterdata = Masterdata.objects.get(Id=random_id)

    return random_masterdata.Id
