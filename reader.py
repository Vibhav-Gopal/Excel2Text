import pandas as p
file = p.read_excel("test.xlsx")
text = open('results.txt','w')

#Change the following value to the number of parts/rows in your discovery matrix
rows = columns = 5


for i in range(rows):
    try:
        affector = list(file[0])[1+i]
    except:
        pass
    for j in range(columns):
        try:
            affectedstat = list(file[1+j])[1+i]
            affected = list(file[1+j])[0]
        except:
            pass
        if affectedstat == 1:
            #print(affector, "Affects", affected)
            text.write(affector+" affects "+affected+'\n')
        pass
