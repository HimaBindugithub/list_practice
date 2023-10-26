def remove_elements():
    print("========================")
    print("Removing the List")
    print("========================")
    global lists_holidays
    lists_holidays=['Dasara','Sankranthi','Christmas','Krishnastami']
    lists_holidays.pop(0)
    print("Removed List is:",lists_holidays)

def access_elements():  
    print("========================")
    print("Accessing the List Elements By Index")
    print("========================")    
    print("Accessing the List elements by using Indexing")
    print("In Sports List Index 0 : ", lists_holidays[0], end = "\n")
    print("In Sports List Index 1 : ", lists_holidays[1], end = "\n")
    print("In Sports List Index 2 : ", lists_holidays[2], end = "\n")
    print(" ")
    print("Accessing the List elements by using Indexing-For Loop ")
    z=0
    for idx in lists_holidays:
            print("In Sports List Index",z,":",idx, end = "\n")
            z=z+1
    print(" ")                
    print("Accessing the List elements by using Indexing-While Loop ")
    j=0
    while j<len(lists_holidays): #0<4
        print("In Sports List Index",j,":",lists_holidays[j], end = "\n")
        j=j+1


def update_elements():
    print("========================")
    print("Updating the List Elements")
    print("========================")    
   
    
    lists_holidays[1]='Dasara'
    print(lists_holidays)




def main():
   
   
    remove_elements()
    access_elements()
    update_elements()


if __name__ == "__main__":
    main()