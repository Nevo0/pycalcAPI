from cmath import log
from random import randrange
from django.shortcuts import render
from django.db.models import Count
import pytz
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer
import json
import datetime
import time
import uuid
from box.models import Box
from order.models import Product, Purchaser,Order, Terminal, Terminals,Gladn, SizeGladn, Gladns,SizeTerminal,TypeTerminal, Component


@api_view(['GET', 'POST'])
def getGlands(request):
    array = []
    if request.method == "POST":
        panels = request.POST.get('panels')
        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        nip = request.POST.get('nip')
        loads = json.loads(panels)
        products=[]
        array.append(loads)
        # code=loads[0]['code']
        if len(loads)>0:
            for element in loads:
                boxs_id=element['id']
                material=element['material']
                quantity=element['quantity']
                status=element['status']
                glands=element['glands']
                terminals=element['terminal']
                selectBox=element['selectBox']
                # print(boxs_id)
                # print(glands)
                # print(terminals)
               
                
                objectTerminals=list(map(lambda x: print_terminals(x,terminals[x]), terminals))
                objectGlands=list(map(lambda x: print_gland(x,glands[x]), glands))

                # sprawdzamy w bazie czy sa takie obiekt jak nie towrzymy je dla terminals i glands
                # terminalObject =addTerminals(terminals)
                glandsObjectt=  addTerminals(glands)
                glandsObjectt=  addTerminals(terminals)



                # print(objectTerminals)
                # print(objectGlands)

                # filtered_list_none_objectTerminals=filtered_list_none(objectTerminals)
                # filtered_list_none_objectGlands=filtered_list_none(objectGlands)
                # filtered_list_none_terminals_sum = sum(filtered_list_none_objectTerminals, [])  
                # filtered_list_none_glands_sum = sum(filtered_list_none_objectGlands, [])  

    routes = [
        "serializerOrder"
    ]
    return Response(routes)


def addTerminals(glandsandterminals):
    
    listaObject=[]    
    if glandsandterminals and len(glandsandterminals) > 0: 
        # print(glandsandterminals)
        for wall, elementogject in glandsandterminals.items():
            # print(wall)
            # return  
            if(wall):
                terminal= getGlandsTerminalsObject(wall, elementogject)
                listaObject.append(terminal)
    print(listaObject)
                # print(elementogject)

def getGlandsTerminalsObject(wall, elements):
    # print(elements)
    lista=[]   
    for element in elements:
        product=  element['product']    
        size=  element['size']
        typ=  element['typ']
        quantity=  element['quantity']
        position=  element['position']          
        if product == "Gland":
            elementObject=(getGland(size,typ))            
        if product == "Terminal":
           elementObject=(getTerminal(size,typ))
        print(elementObject)
    return(lista)
      
        #     purchaser = Purchaser(name= pName,email=email, company_name=company, nip=nip)
        #     purchaser.save()
def getGland(size,typ):      
    checkinname= size+"__"+typ
    try:
        return Gladn.objects.filter(size__name=size, type=typ )
        print(gladn)
    except Gladn.DoesNotExist:
        return create_gland(size,typ, checkinname) 
        
def getTerminal(size,typ):  
    checkinname= size+"__"+typ         
    try:
        return  Terminal.objects.filter(size__name=size,type__name= typ)       
    except Terminal.DoesNotExist:
        return create_terminal(size,typ, checkinname) 
        

def addOrder(purchaser, products):
    # print(products)
    time_now= timeNow()
    emial= purchaser.email
    name= time_now +"__" +emial
    price=oPrice(products)
    order=Order(name=name, price=price , vat= 0 ,purchaser=purchaser)
    order.save() 
    order.product.set(products)
    serializer = OrderSerializer(order, many=False)    
    # print(serializer.data)
    return serializer.data 

def oPrice(purchaser):
    
    price=0
    for element in purchaser:
        price =price + element.price
    return price
def addPurchaser(name ,email, company, nip):
    pName=purchaserName(name ,email)
    try:
       purchaser=Purchaser.objects.get(name=pName)
    except Purchaser.DoesNotExist:
        purchaser = Purchaser(name= pName,email=email, company_name=company, nip=nip)
        purchaser.save()
    # purchaser.component.set([component])
    return purchaser

    pass
def purchaserName(name,email):
    namep= name + "__"+ email
    return namep
    pass

def addProduct( component , selectBox, quantity, box_id):
    id = uuid.UUID(selectBox[0])
    # box=Box.objects.get(id=selectBox[0]).exist()
    try:
       box=Box.objects.get(id=id)       
    except Box.DoesNotExist:
        print("tu trzeba coś wymyślić bo nie może być takiej sytuacji ze nie ma boxa")
        box = None
    name=createProduktName(component , box, quantity)
    price=createProduktprice(component , box, quantity)    
    try:
       product=Product.objects.get(name=name)
       if product.boxs_id != box_id :
            product.boxs_id = box_id
            product.save() 
    except Product.DoesNotExist:
        product = Product(name= name, box=box , quantity=quantity , price= price, boxs_id=box_id)
        product.save()        
        product.component.set([component])
    
    return   product
    
     
def createProduktprice(component , box, quantity):
    componentPrice=component.price
    boxPrice=box.price
    # print(componentPrice)
    # print(boxPrice)
    price= (componentPrice+boxPrice)*quantity
    return price

def createProduktName(component , selectBox, quantity):    
    name= selectBox.name+ "_" + str(quantity)+ "_" + component.name    
    return name
    pass
def addComponent( glands , terminals):
    # print(glands)
    # print(terminals)
    newlistterminals =None
    newlistglands=None
    price= 0
    name=''
    filtered_list_none_gland=filtered_list_none(glands)
    filtered_list_none_terminals=filtered_list_none(terminals)    
    # filtered_list_none_gland = sum(filtered_list_none_gland, [])   
    filtered_list_none_terminals = sum(filtered_list_none_terminals, []) 
    
    if filtered_list_none_gland is not None and len(glands) > 0: 
        price_x=create_price(filtered_list_none_gland)        
        price = price + price_x
        newlistglands = sorted(filtered_list_none_gland, key=lambda x: x.name, reverse=False)
        name = name + create_name(newlistglands)
    if filtered_list_none_terminals is not None and len(filtered_list_none_terminals) > 0: 
        newlistterminals = sorted(filtered_list_none_terminals, key=lambda x: x.name, reverse=False)
        price = price + create_price(newlistterminals)        
        if len(name) > 1  and len(terminals)>0:
            name = name +"--" +create_name(newlistterminals)
        else:
            name = name + create_name(newlistterminals)
    component = Component(name =name,price=price)
    component.save()
     
    # print("test")

    if newlistterminals:
        # print(newlistterminals)
        component.produkt_terminal.set(newlistterminals)
        
    if newlistglands:
        # print(newlistglands)
        component.produkt_glands.set(glands)
        
    # print(price)
    # print(name)
    

    component.save()
    return component
def create_price(glandsOrTerminals):

    
    price= 0
    if glandsOrTerminals != None:        
        for element in glandsOrTerminals:
            if element != None: 
                # print(element)    
                # print(element.price)    
                price =price + element.price
    
    return price

def create_name(glandsOrTerminals):
    name= ''
    if glandsOrTerminals != None:
        for idx, element in enumerate(glandsOrTerminals):        
            # print((idx))
            if element != None:   
                if idx == 0:             
                    name =name + element.name
                else:
                    name =name + "--"+ element.name
    return name


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
    return filtered_list2
    
def print_gland(wall,object):
    
    if len(object)>0:
        return handlerGlands(object)
def print_terminals(wall,object):
    if len(object)>0:
       
        return handlerTerminals(object)
                          
def print_componentsTerminals(the_list):
    list_v= []       
    # print(the_list)
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
        else:            
            # sprawdzić czyt produkt_glands jest pusty 
            if Component.objects.filter(produkt_terminal__isnull=True).exists():
                item=Component.objects.filter(produkt_terminal__isnull=True)                                
                list_v.append(item)
        
    if not list_v:
        return
    return list_v

def print_componentsGlands(the_list):    
    filterlist=filtered_list_none(the_list)    
    list_sum = sum(filterlist, [])   
    list_v= []    

    if list_sum != None and len(list_sum) >0:        
        if Component.objects.filter(produkt_glands__in=list_sum).exists():
            item=Component.objects.filter(produkt_glands__in=list_sum)    
                  
            temp_list=[]
            for el in item:   
                # temp_list.append(el.name)   
                if(len(el.produkt_glands.all())) == (len(list_sum)):                    
                    if not el in list_v:
                        list_v.append(el)
    else:
        
        # sprawdzić czyt produkt_glands jest pusty 
        if Component.objects.filter(produkt_glands__isnull=True).exists():
            
            item=Component.objects.filter(produkt_glands__isnull=True)
            list_v.append(item)
            pass
        else:
            
            pass
    # print(list_v)  
    if not list_v:
        return
    return list_v
  
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
            print("var_create_gland")
            # print(var_create_gland)
            lista.append(create_glands(element, var_create_gland,checkinname, quantity, position))
    return lista

def create_gland(size,typ,checkinname):
    if SizeGladn.objects.filter(name=size).exists():
        print("create_gland")
        print("ustalic cene ")
        price = 10        
        sizeGland= SizeGladn.objects.filter(name=size).first()
        setGlandToDB = Gladn(name = checkinname, type = typ, material = "plastic",size= sizeGland, price =price) 
        # SEND_EMEIL aby uzupełnić prioce
        setGlandToDB.save()
        # print(setGlandToDB.price)                               
        return setGlandToDB
def create_glands(element, glandInDB,checkinname, quantity,position):
    # print(element) 
    # print(glandInDB.price) 
    price= glandInDB.price * quantity  
    gladns = Gladns(name = checkinname+"__"+str(quantity)+"__"+position,  gladn=glandInDB, position = position , price=price, quantity=quantity)
    gladns.save()
    return gladns
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
        # print(sizeTerminal)
        typeTerminal= TypeTerminal.objects.filter(name=typ).first()
        # print(typeTerminal)
        setTerminalToDB = Terminal(name = checkinname, type = typeTerminal, material = "plastic",size= sizeTerminal, price =1)                              
        setTerminalToDB.save()
        return setTerminalToDB
def create_terminals(element, terminalInDB,checkinname, quantity,position):
    price= terminalInDB.price * quantity  
    terminals = Terminals(name = checkinname+"__"+str(quantity)+"__"+position,  terminal=terminalInDB, position = position , price=price, quantity=quantity)
    terminals.save()
    return terminals

def timeNow():
    time_now=datetime.datetime.now(pytz.timezone("Europe/Warsaw")).strftime ("%Y-%m-%d--%H-%M-%S")    
    time2= datetime.datetime.utcnow().timestamp()   
    # print(time2) 
    # print(datetime.tzinfo()) 
    # print(datetime.datetime.now(datetime.timezone.utc))
    # print(datetime.datetime.fromtimestamp(time2).strftime('%Y-%m-%d %H:%M:%S.%f'))
    # print(datetime.datetime.utcfromtimestamp(time2).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    # print(datetime.datetime.utcfromtimestamp(time2).strftime('%Y-%m-%d %H:%M:%S.%f'))
    # print(datetime.datetime.now(pytz.timezone("Europe/Warsaw")).strftime ("%Y-%m-%d--%H-%M-%S"))
    # print(pytz.all_timezones)     
    return time_now    





 


