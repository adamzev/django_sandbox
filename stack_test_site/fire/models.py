from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Team(models.Model):
  name = models.CharField('Name', max_length = 200)

  def __str__(self):
    return self.name

class Firefighter(models.Model):
  RANKS = (
    ('CFO', 'Chief Fire Officer'),
    ('DCFO','Deputy Chief Fire Officer'),
    ('SSO', 'Senior Station Officer'),
    ('SO', 'Station Officer'),
    ('SFF', 'Senior Firefighter'),
    ('QFF', 'Qualified Firefighter'),
    ('FF', 'Firefighter'),
    ('RFF', 'Recruit Firefighter'),
    ('OS', 'Operational Support'),
  )

  STATUS_OPTIONS = (
    ('AV', 'Available'),
    ('OD', 'On Duty'),
    ('UN', 'Unavailable'),
    ('LV', 'Leave'),
  )

  rank = models.CharField("Rank", max_length = 50 , choices=RANKS, default='RFF')
  first_name = models.CharField("First Name", max_length = 200)
  last_name = models.CharField("Last Name", max_length = 200)
  start_date = models.DateField("Start Date")
  status = models.CharField("Status", max_length = 20 , choices=STATUS_OPTIONS, default='Available')
  driver = models.BooleanField('Driver', default=False)
  officer = models.BooleanField('Officer Qualified', default=False)
  teams = models.ManyToManyField(Team)
  order = models.IntegerField('Order')
  

  def __str__(self):
   return self.first_name + ' ' + self.last_name

  class Meta:
        verbose_name = "Firefighter"
        verbose_name_plural = "Firefighters"
