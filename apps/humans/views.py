import re
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import HumanSerializer
from .models import Human

# Create your views here.
class HumanView(APIView):
    serializer = HumanSerializer

    def get(self,request):
        try:
            list = Human.objects.all()                                          #Get all human registers
            serialized = self.serializer(list, many=True)                       #Parse to object format and not queryobject
            return Response(serialized.data, content_type="application/json")
        except:
            return Response(status=500)

    def post(self,request):
        try:
            status = 403 
            if (is_valid_values(request.data['dna'])):                              #Check if adn is valid to be analize need to contain only ACTG characters and new a square matrix
                data = {"dna": request.data['dna'], "mutant": False}                #Set data to register
                if look_patterns(request.data['dna']):                              #If is mutant Set mutant to true and status to 200
                    status = 200                                                
                    data["mutant"] = True
                serializer = HumanSerializer(data = data)                           #Format and validate data
                if (serializer.is_valid()):                                         #if data is valid store it
                    serializer.save()
            else:
                status = 400                                                        #If is not valid data status will be 400
            return Response(status=status)
        except:
            return Response(status=500)

def is_valid_values(dna):       #This function returns true if data is valid and false if is not
    length = len(dna[0])        
    for n in dna:               #Check size of all items must be equal to the numbers of chains and not contain others character tha ACTG
        if (len(n) != length or re.search("([BDEFHIJKMNLOPKRSUVWXYZa-z]|\d\W)",n) ):    
            return False
    return True

def look_patterns(dna):         #This function rearange into sepparates vectors each possibly king of pattern
    is_mutant = False
    founded = 0
    max_size = len(dna[0])      
    cols = [[] for _ in range(max_size)]                    #empty list with max size as numbers of elements
    rows = [[] for _ in range(max_size)]                    #empty list with max size as numbers of elements
    left_diag = [[] for _ in range((max_size * 2) - 1)]     #empty list with max size as double of elements minus one 
    right_diag = [[] for _ in range(len(left_diag))]        #empty list with max size as double of elements minus one 

    for x in range(max_size):                   #Start to mapping the original matrix to vectors
        for y in range(max_size):
            cols[x].append(dna[y][x])
            rows[y].append(dna[y][x])
            left_diag[x+y].append(dna[y][x])
            right_diag[x-y-(-max_size + 1)].append(dna[y][x])

    left_diag = [x for x in left_diag if len(x) >= 4]
    right_diag = [x for x in right_diag if len(x) >= 4]
    
    runs = [cols,rows,left_diag,right_diag]         #Set number of vectors to analize
    for x in runs:                              
        if not is_mutant:                           #If not achive the required number of patterns check the next one
            founded = founded + check_patterns(x)
        if founded >= 2:                            #if is achived it wont continue evaluating
            is_mutant = True
            break
    if is_mutant:                                   #if founded patterns was satisfied return True that means is a mutant
        return True
    else:
        return False

def check_patterns(patterns):                       #This function analize a vector of patterns
        possible = 0                                
        found = 0
        position = 0
        for n in patterns:                          #Read each one and compare ir with the next one until the end of the vector
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
            possible = 0                            #When is read another part of the list reset stats to change the set 
            position = 0
        return found
