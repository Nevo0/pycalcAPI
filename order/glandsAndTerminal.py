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
                objectComponentsglands= print_componentsGlands(objectGlands)
                print(objectComponentsTerminals)
                print(objectComponentsglands)
                # sptawdzić czy to co już mamy jest !!!
                # checkIfIsTerminalmodel


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
def test(x):
    print(x)
def print_gland(wall,object):
    
    if len(object)>0:
        return handlerGlands(object)
def print_terminals(wall,object):
    if len(object)>0:
       
        return handlerTerminals(object)
                          
def print_componentsTerminals(the_list):
    list_v= []
    for each_items in the_list:
        print(each_items)
        item_list = Component.objects.filter(produkt_terminal__in=each_items)
        list_v.append(item_list)
        
    # print(list_v)
    return list_v[0]
def print_componentsGlands(the_list):
    list_v= []
    for each_items in the_list:
        # print(each_items)
        item_lista = Component.objects.filter(product_gladns_site_a__in=each_items)
        item_listb = Component.objects.filter(product_gladns_site_b__in=each_items)
        item_listc = Component.objects.filter(product_gladns_site_c__in=each_items)
        item_listd = Component.objects.filter(product_gladns_site_d__in=each_items)
        # if len(item_listb)>0:
        #     print(len(item_listb))
        #     print((item_listb))


        # print(len(item_lista))
        # print(len(item_listc))
        # print(len(item_listd))

        list_v.append(item_lista)
        
    # print(list_v)
    return list_v[0]
                 


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

