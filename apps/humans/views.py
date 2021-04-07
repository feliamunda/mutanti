import re
from concurrent.futures import Future

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import HumanSerializer
from .models import Human

# Create your views here.
class HumanView(APIView):
    serializer = HumanSerializer

    def get(self,request):
        try:
            list = Human.objects.all()
            serialized = self.serializer(list, many=True)
            return Response(serialized.data, content_type="application/json")
        except:
            return Response(status=500)

    def post(self,request):
        try: 
            status = 403
            data = {"dna": request.data['dna'], "mutant": False}   
            if is_valid_values(request.data['dna']):
                if look_patterns(request.data['dna']):
                    status = 200
                    data["mutant"] = True
            serializer = HumanSerializer(data = data )
            if serializer.is_valid():
                serializer.save()
            return Response(status=status)
        except:
            return Response(status=500)

def look_patterns(dna):
    # thread1 = threading.Thread(target=check_patterns)
    # thread2 = threading.Thread(target=check_patterns)
    is_mutant = False
    founded = 0
    max_size = len(dna[0])
    cols = [[] for _ in range(max_size)]
    rows = [[] for _ in range(max_size)]
    left_diag = [[] for _ in range((max_size * 2) - 1)]
    right_diag = [[] for _ in range(len(left_diag))]

    for x in range(max_size):
        for y in range(max_size):
            cols[x].append(dna[y][x])
            rows[y].append(dna[y][x])
            left_diag[x+y].append(dna[y][x])
            right_diag[x-y-(-max_size + 1)].append(dna[y][x])

    left_diag = [x for x in left_diag if len(x) >= 4]
    right_diag = [x for x in right_diag if len(x) >= 4]
    
    runs = [cols,rows,left_diag,right_diag]
    for x in runs:
        if not is_mutant:
            founded = founded + check_patterns(x)
        if founded >= 2:
            is_mutant = True
            break
    if is_mutant: 
        return True
    else:
        return False

def is_valid_values(dna):
    
    length = len(dna[0])
    for n in dna:
        if (len(n) != length or re.search("([BDEFHIJKMNLOPKRSUVWXYZa-z]|\d\W)",n) ):
            return False
    return True

def check_patterns(patterns):
    possible = 0
    found = 0
    position = 0
    for n in patterns:
        while (position < len(n) - 1):
            if (not n[position + 1]):
                break
            if possible == 3:
                found = found + 1
                possible = 0
            if n[position] == n[position+1]:
                possible = possible + 1
            else:
                possible = 0
            position = position + 1
        possible = 0
        position = 0
    return found
