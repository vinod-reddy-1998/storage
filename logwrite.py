from datetime import datetime
start_date=input("enter the start date in format of 'dd/mm/yy: '")
start_datetime_obj = datetime.strptime(start_date, "%d/%m/%y")

end_date=input("enter the start date in format of 'dd/mm/yy: '")
end_datetime_obj = datetime.strptime(end_date, "%d/%m/%y")
gen=False
def Convert_dict(lst):
    res_dct = {}
    for item in lst:
        if item not in res_dct:
            res_dct[item]=1
        else:
            res_dct[item]=res_dct[item]+1
    return (res_dct)

day_count_dict={}
global_list=[]
global_dict={}

log_file_path = "auto_rehab_2.log"
p=0
gen=False   

with open(log_file_path, "r") as file:
    new_temp_list=[]
    log_contents = file.readlines()
    for (index,line) in enumerate(log_contents):
        if line.startswith("Run started at:"):
            my_date=line[16:40]
            
            datetime_obj = datetime.strptime(my_date, "%a %b %d %H:%M:%S %Y")
            if datetime_obj>=start_datetime_obj and datetime_obj<=end_datetime_obj:
                # print(datetime_obj)
                get_date=datetime_obj.strftime("%d-%m")
                print("*"*80)
                print(line)
                gen=True
                # print(index,line,gen)
        if line.startswith("Successes") and gen:
            print(line)
            temp_list=[]
            p=int(line.split("(")[1].split(")")[0])
            for i in range(1,p+1):
                k=(log_contents[index+i]).split("(")[1].split(" ")[0].split(")")[0]
                temp_list.append(k)            
            dic=Convert_dict(temp_list)
            print(temp_list)
            print(datetime_obj)
            global_list.append((str(datetime_obj).split()[0],temp_list))

            for key,value in dic.items():
                print(key,"=>",value)
        
            gen=False

print(global_list)
new_list=[]

for i in range(len(global_list)-1):
    # print(global_list[i][1],"vinod")
    if global_list[i][0]==global_list[i+1][0]:
        # print(global_list[i],"vinod")
        new_list.extend(global_list[i][1])
    else:
        new_list.extend(global_list[i][1])
        global_dict[global_list[i][0]]=new_list
        new_list=[]
# print(global_dict)
new_global_dict={}
for key,value in global_dict.items():
    new_global_dict[key]=Convert_dict(value)
# print(new_global_dict)25
for key,value in new_global_dict.items():
    print(key,value)



