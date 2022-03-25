from cmath import log
from random import randrange
from django.shortcuts import render
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import datetime
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
                material=element['material']
                quantity=element['quantity']
                status=element['status']
                glands=element['glands']
                terminals=element['terminal']
                selectBox=element['selectBox']
                # print(glands)
               
                
                objectTerminals=list(map(lambda x: print_terminals(x,terminals[x]), terminals))
                objectGlands=list(map(lambda x: print_gland(x,glands[x]), glands))

                filtered_list_none_objectTerminals=filtered_list_none(objectTerminals)
                filtered_list_none_objectGlands=filtered_list_none(objectGlands)
                filtered_list_none_terminals_sum = sum(filtered_list_none_objectTerminals, [])  
                filtered_list_none_glands_sum = sum(filtered_list_none_objectGlands, [])  

                
                objectComponentsTerminals= print_componentsTerminals(objectTerminals)
                objectComponentsglands= print_componentsGlands(objectGlands)

                # print(filtered_list_none_terminals_sum)
                # print(filtered_list_none_glands_sum)
                len_terminals=len(filtered_list_none_terminals_sum)
                len_glands=len(filtered_list_none_glands_sum)
                component = Component.objects.filter(
                    produkt_glands__in=filtered_list_none_glands_sum,                    
                )               
                
                len_terminals=len(filtered_list_none_terminals_sum)
                len_glands=len(filtered_list_none_glands_sum)
                # print(filtered_list_none_glands_sum)
                # print(filtered_list_none_terminals_sum)
                # print(len_glands)
                # print(len_terminals)
               
                component_filter = Component.objects.annotate(count=Count('produkt_glands')).filter(count=len_glands)
                # print(component_filter)  
                
                component_filter = component_filter.annotate(count=Count('produkt_terminal')).filter(count=len_terminals)
                # print(component_filter)    
                # print(component_filter[0].produkt_terminal.all())
                      

                if len_terminals>0:                    
                    component_filter = component_filter.filter(
                        produkt_terminal__in=filtered_list_none_terminals_sum,                    
                    )
                if len_glands>0:                    
                    component_filter = component_filter.filter(
                            produkt_glands__in=filtered_list_none_glands_sum,                    
                        )                
                
                # print(component_filter2)
                len_component_filter=len(component_filter)
                
                
                if len_component_filter == 1:
                    component_filter= component_filter.first()
                    # print(component_filter)
                    # jest taki w bazie 
                    pass
                elif len_component_filter == 0:
                    objectGlands=filtered_list_none(objectGlands)
                    # objectTerminals=filtered_list_none(objectTerminals)
                    # print("objectGlands")
                    objectGlandslist=sum(objectGlands, [])  
                    component_filter =addComponent( objectGlandslist, objectTerminals)
                    # create components
                    pass
                else:
                    print('jakas maskra')
                    component_filter= component_filter.first()
                    pass
                    # jakas maskra
                # print(component_filter)
                product=addProduct( component_filter , selectBox, quantity)
                # print(product) 
                products.append(product)
            # print(loads)
            
           
            getPurchaser=addPurchaser(name ,email, company, nip)
            addOrder(getPurchaser, products)

    routes = [
        "glands"
    ]
    return Response(routes)
def addOrder(purchaser, products):
    time= datetime.datetime.now().strftime ("%Y-%m-%d--%H-%M-%S")    
    emial= purchaser.email
    name= time +"__" +emial
    price=oPrice(products)
    order=Order(name=name, price=price , vat= 0 ,purchaser=purchaser)
    order.save()
    order.product.set(products)
    return
    
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

def addProduct( component , selectBox, quantity):
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
    except Product.DoesNotExist:
        product = Product(name= name, box=box , quantity=quantity , price= price)
        product.save()
        product.component.set([component])
    
    return   product
    
     
def createProduktprice(component , box, quantity):
    componentPrice=component.price
    boxPrice=box.price
    print(componentPrice)
    print(boxPrice)
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
            print(var_create_gland)
            lista.append(create_glands(element, var_create_gland,checkinname, quantity, position))
    return lista

def create_gland(size,typ,checkinname):
    if SizeGladn.objects.filter(name=size).exists():
        print("xxx")
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
    price= glandInDB.price * quantity * 2   
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
    price= terminalInDB.price * quantity * 2   
    terminals = Terminals(name = checkinname+"__"+str(quantity)+"__"+position,  terminal=terminalInDB, position = position , price=price, quantity=quantity)
    terminals.save()
    return terminals





 


