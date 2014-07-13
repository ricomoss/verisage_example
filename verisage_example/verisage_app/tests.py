from django.test import TestCase
from fixtureless import Factory

import models


class TestStructureSetup(TestCase):
    def _create_persons(self):
        # Create data specific person objects
        initial1 = {
            '_first_name': 'john',
            '_last_name': 'doe',
            'capacity': 1.22
        }
        initial2 = {
            '_first_name': 'jane',
            '_last_name': 'doe',
            'capacity': 1.54
        }
        self.person1, self.person2 = self.factory.create(
            models.Person, (initial1, initial2))

        # Create 10 other random person objects
        self.factory.create(models.Person, 10)

    def _create_projects(self):
        # Create data specific project objects
        initial1 = {
            'tech_lead': self.person1,
            'name': 'tech_lead1',
            'effort_estimate': 1.25,
        }
        initial2 = {
            'tech_lead': self.person2,
            'name': 'tech_lead2',
            'effort_estimate': 1.55,
        }
        self.project1, self.project2 = self.factory.create(
            models.Project, (initial1, initial2))

        # Create 10 other random project objects
        self.factory.create(models.Project, 10)

    def _create_assignments(self):
        # To create projects you must first create other required objects
        self._create_projects()

        # Create data specific assignment objects
        initial1 = {
            'project': self.project1,
            'name': 'test_project1'
        }
        initial2 = {
            'project': self.project2,
            'name': 'test_project2'
        }
        self.assignment1, self.assignment2 = self.factory.create(
            models.Assignment, (initial1, initial2))

        # Create 10 other random assignment objects
        self.factory.create(models.Assignment, 10)

    def _create_commitments(self):
        # To create commitments you must first create other required objects
        self._create_persons()
        self._create_assignments()

        # Create data specific commitment objects
        initial1 = {
            'assigned_to': self.person1,
            'assignment': self.assignment1,
        }
        initial2 = {
            'assigned_to': self.person2,
            'assignment': self.assignment2,
        }
        self.commitment1, self.commitment2 = self.factory.create(
            models.Commitment, [initial1, initial2])

        # Create 10 other commitments for good measure
        self.factory.create(models.Commitment, 10)

    def setUp(self):
        self.factory = Factory()
        self._create_commitments()


class PersonTest(TestStructureSetup):
    def setUp(self):
        super(PersonTest, self).setUp()
        initial = {
            '_first_name': 'guido',
            '_last_name': 'van rossum',
            'capacity': 100,
        }
        self.person3 = self.factory.create(models.Person, initial)

    def test_person(self):
        guido_projects = models.Project.objects.filter(tech_lead=self.person3)
        self.assertEqual(len(guido_projects), 0)

        self.assertEqual(models.Person.objects.all().count(), 13)

        self.assertEqual(
            models.Person.objects.filter(_first_name='john').count(), 1)


class SkillTest(TestStructureSetup):
    def test_skill(self):
        self.assertEqual(models.Skill.objects.all().count(), 0)

        skill = self.factory.create(models.Skill)
        self.person1.skills.add(skill)
        self.person1.save()

        self.assertEqual(
            models.Skill.objects.all().count(),
            self.person1.skills.all().count())

        self.assertEqual(self.person1.skills.all().count(), 1)

