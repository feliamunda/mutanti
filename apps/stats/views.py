from rest_framework.response import Response
from rest_framework.views import APIView

from apps.humans.models import Human

# Create your views here.

class HumanStatsView(APIView):

    def get(self,request):      
        try:
            count_human_dna = Human.objects.count()                                         #Count all registers
            count_mutant_dna = Human.objects.filter(mutant=True).count()                    #Count all mutants
            if count_human_dna == 0:                                                        #If no count will throw a error because 0/0 will generate it so set manually to zero
                ratio = 0
            else:
                ratio = round((count_mutant_dna / count_human_dna),2)                       #Otherwise Calculate relation
            data = {"count_mutant_dna":count_mutant_dna, "count_human_dna":count_human_dna, "ratio":ratio}  #Format Response
            return Response(data, content_type="application/json")                             
        except:
            return Response(status=500)      