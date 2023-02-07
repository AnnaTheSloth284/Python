# Program to create whatsapp dm links 
# for rows of names and contact numbers 

# Input should be in the format
# Naira Kareem	8500809500
# Considering excel sheet it should be
# a row of two adjacent columns while copying the data

def createwalink(f1):
    #f1= input()
    l1=f1.split()
    #print(l1)
    length=len(l1)
    for i in range(0,length-1):
        print(l1[i],end=" ")
    walink = "wa.me/+91"+l1[length-1]
    print(walink)

l0='''Replace this text with data rows''' # Enter rows of data here by
                                          # replacing this text within the multiline
                                          # comment's triple inverted commas
                                          # (Just Ctrl+Shift+C AND Ctrl+Shift+V the rows)
ll0=l0.split("\n")
#print(ll0)
for i in ll0:
    i.replace("\t"," ")
    #print(i)
    createwalink(i)
