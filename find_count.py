def Convert_dict(lst):
    res_dct = {}
    for item in lst:
        if item not in res_dct:
            res_dct[item]=1
        else:
            res_dct[item]=res_dct[item]+1
    return (res_dct)
import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('demo_6.xlsx')

# Access the values of two columns
column1 = df['Created']
column2 = df['Jenkins']

global_list=[]
for value1, value2 in zip(column1, column2):
    p=[str(value1.date()), value2]
    global_list.append(p)
# print(global_list)
global_dict={}
new_list=[]

for i in range(len(global_list)-1):
    if global_list[i][0]==global_list[i+1][0] and global_list[i][1]!="":
        # print(global_list[i][1])
        new_list.append(global_list[i][1])
    else:
        new_list.append(global_list[i][1])
        global_dict[global_list[i][0]]=new_list
        new_list=[]
# print(global_dict)
new_global_dict={}
for key,value in global_dict.items():
    new_global_dict[key]=Convert_dict(value)
# print(new_global_dict)25
for key,value in new_global_dict.items():
    print(key,"=>",value)


