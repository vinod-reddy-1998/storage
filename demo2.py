def strip(word):
    return word.strip()
def find_jenkin(k):
    jen=["master","rel3-1-x","rel3-3-x","rel4-1-a-staging","rel4-0-x","rel4-1-x","perf","smb","controlplane","kernel","objectstore","replication","simulator","ui","tf","core-data-services","ubuntu18","build","meteor","sandbox","sanbox","legend"]
    word=list(set(k).intersection(set(jen)))
    if len(word)==2 and "legend" in word:
        word.remove("legend")
        word=word[0]
    elif len(word)>0:
        word=word[0]
    return word

def find_hardware(k):
    given=["norway","norway-hw","legend","legend-hw"]
    word_list=list(set(k).intersection(set(given)))
    # print(word_list)
    word=""
    if len(word_list)>0:
        word=word_list[0]

        if word[-3:]=="-hw":
            word=word[:-3]
        # print(word)
    return word

from openpyxl import load_workbook
workbook = load_workbook(filename='demo_6.xlsx')
workbook1=workbook.active
sheet = workbook.worksheets[0]
row_label="I"
row = sheet[row_label]

i=0
cl=0
jl=0

for cell in row:
    if cell.value!=None:
        # k=(cell.value).split(",")
        k=list(map(strip,cell.value.split(",")))
        if "manual-rehab" in (cell.value):
            k.remove("manual-rehab")
        # print(k)
        for item in k:
            if item.startswith("irp") or item.startswith(" irp"):
                cluster_name=workbook1['K'][i]
                cluster_name.value=item
        i+=1
        jen=find_jenkin(k)

        if jen:
            cluster_name=workbook1['L'][jl]
            cluster_name.value=jen
            k.remove(jen)
        jl+=1
        word=find_hardware(k)
        if word:
            cluster_name=workbook1['M'][cl]
            cluster_name.value=word
        cl+=1
        print(k)
workbook.save("demo_6.xlsx")
workbook.close()