import random
def avarage_partition(list):
    data_list = []
    data_list_dic = {}
    for i in list:
        if i not in data_list_dic:
            data_list_dic[i] = 1
            data_list.append(i)
        else:
            data_list_dic[i]+= 1

    list = efi_ord_two(data_list)
    ld = []
    for i in list:
        for rep in range(0,data_list_dic[i]):
            ld.append(i)
    return ld

def efi_ord_two(list):       
    if len(list) < 3:               
        if(len(list) == 1):
            return list;
        if len(list) == 2:
            if list[0] > list[1]:
                return [list[1]] + [list[0]]
            else:
                return [list[0]] + [list[1]]
    else:   
        lista_ordenada = []
        lista_iz = []
        lista_der = []
        media = 0
        index = 0

        veces = list.count(list[0])

        if veces == len(list):
            return list

        for i in list:
            media = media + i

        for i in list:
            index +=1   
            if (media//len(list)) >= i:                            
                lista_iz.append(i)
            else:                                 
                lista_der.append(i)  
    
        return efi_ord_two(lista_iz) + efi_ord_two(lista_der)
        
list = [] 

for i in range(0,1000000):
        x = (int(random.random()*100000))
        list.append(x)


print(list)
print(efi_ord_two(list))