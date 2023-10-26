def create_list():
    print("====================================")
    print("Creating list")
    print("====================================")
    global lists_billionaires
    lists_billionaires= ['Elon Musk','Bill Gates','Jeff Bezos','Mukesh Ambani']
    print("Created list is:",lists_billionaires)
def display_list():
    print("====================================")
    print("Accessing list")
    print("====================================")      
    print("Accessing the List elements by using Indexing")
    print("In Sports List Index 0 : ", lists_billionaires[0], end = "\n")
    print("In Sports List Index 1 : ", lists_billionaires[1], end = "\n")
    print("In Sports List Index 2 : ", lists_billionaires[2], end = "\n")
    print("In Sports List Index 3 : ", lists_billionaires[3], end = "\n")
    print("Accessing the List elements by using Indexing-For Loop ")
    x=0
    for ele in lists_billionaires:
            print("In Sports List Index:",x, ele, end = "\n")
            x=x+1
               
    print("Accessing the List elements by using Indexing-While Loop ")
    i=0
    while i<len(lists_billionaires): #0<4
        print("In Sports List Index:",i,lists_billionaires[i], end = "\n")
        i=i+1


 
create_list()
display_list()

