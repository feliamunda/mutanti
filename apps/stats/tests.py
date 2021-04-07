from django.test import TestCase, Client
from django.db import connection
from apps.humans.models import Human
from .apps import StatsConfig

# Create your tests here.
class StatsTestCase(TestCase):
        
    def test_stats_shoud_response_all_zeros(self):
        """if i get stats without any register"""
        c = Client()
        response = c.get('/stats/')
        for x in response.data:
            self.assertEqual(response.data[x], 0)
    
    def test_stats_shoud_response_correct_ratio(self):
        """if i get stats and ratio from 1 mutant and 4 samples between them"""
        Human.objects.create(dna=['ATGC','CAGT','TTGT','AGGG'],mutant=True)
        Human.objects.create(dna=['ATGC','CAGT','TTGT','AGGG'])
        Human.objects.create(dna=['ATGC','CAGT','TTGT','AGGG'])
        Human.objects.create(dna=['ATGC','CAGT','TTGT','AGGG'])

        ratio = 1/4
        c = Client()
        response = c.get('/stats/')
        self.assertEqual(response.data['ratio'], ratio)
        self.assertEqual(response.data['count_human_dna'], 4)
        self.assertEqual(response.data['count_mutant_dna'], 1)
    
    def test_stats_shoud_response_status_500(self):
        """the response should be a status code invalid"""
        human = Human()
        cursor = connection.cursor()
        table_name = human._meta.db_table
        sql = "DROP TABLE %s;" % (table_name, )
        cursor.execute(sql)    
        c = Client()
        response = c.get('/stats/')
        self.assertEqual(response.status_code,500)
    
    def app_name_should_be_stats(self):
        """the app name should be stats"""
        self.assertEqual(StatsConfig.name,"stats")