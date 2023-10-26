def create_list():
    print("========================")
    print("Creating the List")
    print("========================")
    global listsports
    listsports=[ ]
    print("Created List is:",listsports)
def generate_elements():
    print("=======================================")
    print("Assigning the List Elements Manually:")
    print("=======================================")
    """
     listsports[0]='Cricket'
     listsports[1]='Foot Ball'
     listsports[2]='Shuttle'
     listsports[3]='Base Ball'
     #IndexError: list index out of range
   
     listsports[0].append('Cricket')
     listsports[1].append('Foot Ball')
     listsports[2].append('Shuttle')
     listsports[3].append('Base Ball')
     
     listsports[0].extend('Cricket')
     listsports[1].extend('Foot Ball')
     listsports[2].extend('Shuttle')
     listsports[3].extend('Base Ball')
     # Below Method is inserting elements character wise
     listsports.extend('Cricket')
     listsports.extend('Foot Ball')
     listsports.extend('Shuttle')
     listsports.extend('Base Ball')
    """
    listsports.append('Cricket')
    listsports.append('Foot Ball')
    listsports.append('Shuttle')
    listsports.append('Base Ball')
    print("Generated List is:",listsports)



def update_elements():
    print("========================")
    print("Updating the List Elements")
    print("========================")    
    listsports[0]='Base Ball'
    listsports[1]='Shuttle'
    listsports[2]='Foot Ball'
    listsports[3]='Cricket'
    print(listsports)
       
def access_list():  
    print("========================")
    print("Accessing the List Elements")
    print("========================")    
    print("Accessing the List elements by using Indexing")
    print("In Sports List Index 0 : ", listsports[0], end = "\n")
    print("In Sports List Index 1 : ", listsports[1], end = "\n")
    print("In Sports List Index 2 : ", listsports[2], end = "\n")
    print("In Sports List Index 3 : ", listsports[3], end = "\n")
    print(" ")
    print("Accessing the List elements by using Indexing-For Loop ")
    x=0
    for ele in listsports:
            print("In Sports List Index",x,":",ele, end = "\n")
            x=x+1
    print(" ")                
    print("Accessing the List elements by using Indexing-While Loop ")
    i=0
    while i<len(listsports): #0<4
        print("In Sports List Index",i,":",listsports[i], end = "\n")
        i=i+1
def main():
    #call the create_list()
    create_list()

    generate_elements()
    access_list()
    update_elements()
    access_list()
    


if __name__ == "__main__":
    main()
