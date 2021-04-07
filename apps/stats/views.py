from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.humans.models import Human

# Create your views here.

class HumanStatsView(APIView):

    def get(self,request):
        try:
            count_human_dna = Human.objects.count()
            count_mutant_dna = Human.objects.filter(mutant=True).count()
            if count_human_dna == 0:
                ratio = 0
            else:
                ratio = "{:.2f}".format(count_mutant_dna / count_human_dna)
            data = {"count_mutant_dna":count_mutant_dna, "count_human_dna":count_human_dna, "ratio":ratio}
            return Response(data, content_type="application/json")
        except:
            return Response(status=500)