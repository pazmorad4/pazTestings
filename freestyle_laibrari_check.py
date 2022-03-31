
my_dic = {'shai':{},'iris':{},'ouzi':{}}

getlist = 'iris'
getlist2=['paz','fkd','paz']
index = 0x
list=['shai','iris']

for upperkey in list:
    for key,value in my_dic[upperkey].items():
        if upperkey == getlist and key == getlist2[index]:
            my_dic[upperkey][getlist2] = 1


index =+ 1
print(my_dic)