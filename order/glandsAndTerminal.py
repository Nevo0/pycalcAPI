from cmath import log
from random import randrange
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from order.models import Terminal, Terminals,Gladn, SizeGladn, Gladns,SizeTerminal,TypeTerminal, Component


@api_view(['GET', 'POST'])
def getGlands(request):
    array = []
    if request.method == "POST":
        panels = request.POST.get('panels')
        loads = json.loads(panels)

        array.append(loads)
        # code=loads[0]['code']
        if len(loads)>0:
            for element in loads:
                material=element['material']
                quantity=element['quantity']
                status=element['status']
                glands=element['glands']
                terminals=element['terminal']
                selectBox=element['selectBox']
               
                objectTerminals=list(map(lambda x: print_terminals(x,terminals[x]), terminals))
                objectGlands=list(map(lambda x: print_gland(x,glands[x]), glands))
                # print(type(objectGlands))
                # print(objectTerminals)
                # objectComponents=map(lambda x: print_components(x,objectTerminals[x]), objectTerminals)
                # result = map(print_components, objectTerminals)

                objectComponentsTerminals= print_componentsTerminals(objectTerminals)
                objectComponentsglands= print_componentsGlands(objectGlands, objectComponentsTerminals)
                print(objectComponentsTerminals)
                # print(objectTerminals)

                # sptawdzić czy to co już mamy jest !!!
                # checkIfIsTerminalmodel
                # if sala in beer.salas_set.all():
                #     pass


                pass
                # print("-----------------------------")
                # print(objectComponentsTerminals[0].exclude('name'))
                # print(objectComponentsTerminals[0].values()[1])
                # print(objectComponentsTerminals[0].values()[2])
                # print("-----------------------------")
                # print(objectComponentsTerminals[0].values_list())
                # print("-----------------------------0")
                # print(objectComponentsTerminals)
                # print("-----------------------------")
                # print("-----------------------------")

                    
                
                
                
                # print(loads[0]['code'])
    
    routes = [
        "glands"
    ]
    return Response(routes)
@api_view(['GET', 'POST'])
def getTerminals(request):
    print(request)
    routes = [
        "getTerminals"
    ]
    return Response(routes)
def  filtered_list_none(sample_list):
    # initialize filtered list
    filtered_list2 = []

    # Using for loop
    for ele in sample_list:
        if ele != None:
            filtered_list2.append(ele)
    
def print_gland(wall,object):
    
    if len(object)>0:
        return handlerGlands(object)
def print_terminals(wall,object):
    if len(object)>0:
       
        return handlerTerminals(object)
                          
def print_componentsTerminals(the_list):
    list_v= []   
    for each_items in the_list:
        if each_items != None:            
            if Component.objects.filter(produkt_terminal__in=each_items).exists():
                item=Component.objects.filter(produkt_terminal__in=each_items)
                # print(item)
                for el in item:   
                    # temp_list.append(el.name)   
                    if(len(el.produkt_terminal.all())) == (len(each_items)):                    
                        if not el in list_v:
                            list_v.append(el)
        
    if not list_v:
        return
    return list_v

def print_componentsGlands(the_list, objectComponentsTerminals):
    list=filtered_list_none(the_list)
    print(list)
    print(the_list)
    list_v= []
    for each_items in the_list:
        if each_items != None:
            # print(each_items)
            if Component.objects.filter(produkt_glands__in=each_items).exists():
                item=Component.objects.filter(produkt_glands__in=each_items)
                
                temp_list=[]
                for el in item:   
                    # temp_list.append(el.name)   
                    if(len(el.produkt_glands.all())) == (len(each_items)):                    
                        if not el in list_v:
                            list_v.append(el)
    if not list_v:
        return
    return list_v
                 


def create_gland(size,typ,checkinname):
    if SizeGladn.objects.filter(name=size).exists():
        price = create_price(size)        
        sizeGland= SizeGladn.objects.filter(name=size).first()
        setGlandToDB = Gladn(name = checkinname, type = typ, material = "plastic",size= sizeGland, price =price) 
        # SEND_EMEIL aby uzupełnić prioce
        # print(setGlandToDB)                               
        setGlandToDB.save()
        return setGlandToDB
    

def create_glands(element, glandInDB,checkinname, quantity,position):
    price= glandInDB.price * quantity * 2   
    gladns = Gladns(name = checkinname+"__"+str(quantity)+"__"+position,  gladn=glandInDB, position = position , price=price, quantity=quantity)
    gladns.save()
    return gladns

def handlerGlands(object):   
    lista=[]
    for element in object:        
        size=  element['size']
        typ=  element['typ']
        quantity=  element['quantity']
        position=  element['position']
        checkinname= size+"__"+typ
        if Gladn.objects.filter(name=checkinname).exists():
            glandInDB = Gladn.objects.filter(name=checkinname).first()
            checkinnameGlands= glandInDB.name +"__"+str(quantity)+"__"+position
            # print(checkinnameGlands)
            if  Gladns.objects.filter(name=checkinnameGlands).exists():
                
                lista.append(Gladns.objects.filter(name=checkinnameGlands).first()     )              
            else:
                lista.append(create_glands(element, glandInDB,checkinname, quantity, position))
        else:
            var_create_gland=create_gland(size,typ, checkinname) 
            lista.append(create_glands(element, var_create_gland,checkinname, quantity, position))
    return lista
def handlerTerminals(object):   
    lista=[]
    for element in object:  
        
        
        size=  element['size']
        typ=  element['typ']
        quantity=  element['quantity']
        position=  element['position']
        checkinname= size+"__"+typ      
        # print(element)
        if Terminal.objects.filter(name=checkinname).exists():
            terminaldInDB = Terminal.objects.filter(name=checkinname).first()
            checkinnameGlands= terminaldInDB.name +"__"+str(quantity)+"__"+position     
            # sprawdzamy czy w terminalach mamy terminal
            if  Terminals.objects.filter(name=checkinnameGlands).exists():
                # jesli jest taki terminals to dodajemy go do listy
               
                lista.append(Terminals.objects.filter(name=checkinnameGlands).first()     )              
            else:
                # jesli nie ma terminals to tworzymy nowy 
                lista.append(create_terminals(element, terminaldInDB,checkinname, quantity, position))

            pass
        else:
            # Jeśli taki typ terminala nie istnieje      
            # dodajemy go do termianl
            # i tworzymy terminals       
            var_create_terminal=create_terminal(size,typ, checkinname) 

            lista.append(create_terminals(element, var_create_terminal,checkinname, quantity, position))
    return lista
def create_terminal(size,typ,checkinname):    
    if SizeTerminal.objects.filter(name=size).exists():              
        sizeTerminal= SizeTerminal.objects.filter(name=size).first()
        print(sizeTerminal)
        typeTerminal= TypeTerminal.objects.filter(name=typ).first()
        print(typeTerminal)
        setTerminalToDB = Terminal(name = checkinname, type = typeTerminal, material = "plastic",size= sizeTerminal, price =1)                              
        setTerminalToDB.save()
        return setTerminalToDB
def create_terminals(element, terminalInDB,checkinname, quantity,position):
    price= terminalInDB.price * quantity * 2   
    terminals = Terminals(name = checkinname+"__"+str(quantity)+"__"+position,  terminal=terminalInDB, position = position , price=price, quantity=quantity)
    terminals.save()
    return terminals





 
def create_price(size):
    x = size.split("m")
    return (int(x[1])*randrange(10,12)  )

