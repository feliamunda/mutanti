from django.test import TestCase, Client
from django.db import connection
from .models import Human
from .serializers import HumanSerializer
from .views import HumanView
from .apps import HumansConfig

# Create your tests here.

class HumanTestCase(TestCase):
    def setUp(self):
        Human.objects.create(dna=['ATGCGA','CAGTGC','TTATGT','AGAAGG','CCCCTA','TCACTG'],mutant=True)
        Human.objects.create(dna=['ATGC','CAGT','TTGT','AGGG'])
    
    def app_name_should_be_humans(self):
        """the app name should be human"""
        self.assertEqual(HumansConfig.name,"humans")
        
    def test_dna_creates_no_mutant_default(self):
        """if is passed mutant is true otherwise is false"""
        dna1 = Human.objects.get(dna=['ATGCGA','CAGTGC','TTATGT','AGAAGG','CCCCTA','TCACTG'])
        dna2 = Human.objects.get(dna=['ATGC','CAGT','TTGT','AGGG'])
        self.assertTrue(dna1.mutant)
        self.assertFalse(dna2.mutant)
    
    def test_dna_creates_date(self):
        """if adn register occurs it should add date automatically"""
        dna = Human.objects.get(dna=['ATGCGA','CAGTGC','TTATGT','AGAAGG','CCCCTA','TCACTG'])
        self.assertTrue(dna.created_at)
    
    def test_dna_should_return_all_objects_from_database_serialized(self):
        """if get is requested should return all registers"""
        c = Client()
        serializer= HumanSerializer(Human.objects.all(), many=True)
        response = c.get('/mutants/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
    
    def test_dna_should_return_all_objects_from_database_serialized(self):
        """if get is requested should return all registers"""
        c = Client()
        serializer= HumanSerializer(Human.objects.all(), many=True)
        response = c.get('/mutants/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_dna_should_return_application_json(self):
        """the response should be application json"""
        c = Client()
        response = c.get('/mutants/')
        self.assertEqual(response.content_type,"application/json")
    
    def test_dna_should_return_status_403(self):
        """the response should be a status code invalid"""
        c = Client()
        response = c.post('/mutants/',{"dna":["ATGC","CAGT","TTGT","AGTG"]})
        self.assertEqual(response.status_code,403)
    
    def test_dna_post_should_return_error_500(self):
        """the response should be a status code 500 Server Error"""
        human = Human()
        cursor = connection.cursor()
        table_name = human._meta.db_table
        sql = "DROP TABLE %s;" % (table_name, )
        cursor.execute(sql)
        c = Client()
        response = c.post('/mutants/',{"dna":["ATGC","CAGT","TTGT","AGTG"]})
        self.assertEqual(response.status_code,500)
    
    def test_dna_get_should_return_500(self):
        """the response should be a status code 500 Server Error"""
        human = Human()
        cursor = connection.cursor()
        table_name = human._meta.db_table
        sql = "DROP TABLE %s;" % (table_name, )
        cursor.execute(sql)
        c = Client()
        response = c.get('/mutants/')
        self.assertEqual(response.status_code,500)
    
    
        