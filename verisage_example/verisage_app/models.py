from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Group(models.Model):
    name = models.CharField(max_length=25)


class User(AbstractUser):
    group = models.ForeignKey(Group, null=True, blank=True)


class Skill(BaseModel):
    name = models.CharField(max_length=25)


class RelativeDurationEntity(BaseModel):
    relative_end_date = models.IntegerField()
    relative_start_date = models.IntegerField()


class AllocationEntity(models.Model):
    pass


class Person(AllocationEntity, BaseModel):
    _user = models.OneToOneField(User)
    _first_name = models.CharField(max_length=25)
    _last_name = models.CharField(max_length=25)
    capacity = models.FloatField()
    skills = models.ManyToManyField(Skill)


class DurationEntity(BaseModel):
    end_date = models.DateField()
    start_date = models.DateField()


class Project(DurationEntity):
    tech_lead = models.ForeignKey(Person)
    name = models.CharField(max_length=25)
    effort_estimate = models.FloatField()


class Assignment(AllocationEntity, RelativeDurationEntity):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=25)


class Duration(RelativeDurationEntity):
    parent = models.ForeignKey('Duration', null=True, blank=True)
    number_hours_per_day = models.FloatField()


class Commitment(AllocationEntity, RelativeDurationEntity):
    assignment = models.ForeignKey(Assignment)
    assigned_to = models.ForeignKey(Person)
