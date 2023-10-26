# 1.Create a List Empty List.
# 2.Generate a Elements.
# 3.Access the Elements.
# 4.Update the Elemensts.
# 5.Check the updated Elemensts.
# 6.add new elements .
# 7.insert new elements at particular position.
# 8.Delete the element at particular position.
# 9.access the element at particular position.
# 10.pop the element.


# 1.Create a List Empty List.
def createlist():
    print("=======================")
    print("Creating An Empty List")
    print("=======================")
    global presidents_india
    presidents_india=[]
    print("")
    print("Created An Empty List:",presidents_india)
    print("")

# 2.Generate a Elements.
def generateitems():
    print("====================================")
    print("Generating An Items Into The  List")
    print("====================================")
    print("")
    presidents_india.extend(['Rajendra Prasad','Sarvepalli Radha Krishna','Zakir Husain','Varahagiri Venkata GIri','Hidayatullah','Fakhruddin Ali Ahmed','B.D.Jatti','Neelam Sanjiva Reddy','Giani Zail Singh','Venkataraman','Shankar Dayal Sharma','K.R.Narayan','Pranab Mukherjee'])
    print("Generated List:",presidents_india)
    print("")

# 3.Access the Elements.
def printitems():
    print("====================================")
    print("Accessing Items From The  List")
    print("====================================")
    print("")
    print("In Presidents Of India List Index 0 :",presidents_india[0],end="\n")
    print("In Presidents Of India List Index 1 :",presidents_india[1],end="\n")
    print("In Presidents Of India List Index 2 :",presidents_india[2],end="\n")
    print("In Presidents Of India List Index 3 :",presidents_india[3],end="\n")
    print("In Presidents Of India List Index 4 :",presidents_india[4],end="\n")
    print("In Presidents Of India List Index 5 :",presidents_india[5],end="\n")
    print("In Presidents Of India List Index 6 :",presidents_india[6],end="\n")
    print("In Presidents Of India List Index 7 :",presidents_india[7],end="\n")
    print("In Presidents Of India List Index 8 :",presidents_india[8],end="\n")
    print("In Presidents Of India List Index 9 :",presidents_india[9],end="\n")
    print("In Presidents Of India List Index 10:",presidents_india[10],end="\n")
    print("In Presidents Of India List Index 11:",presidents_india[11],end="\n")
    print("In Presidents Of India List Index 12:",presidents_india[12],end="\n")
    print(" ")    

# 4.Update the Elemensts.

def modifyingelements():
    print("====================================")
    print("Updating Elements In The  List")
    print("====================================")
    print("")
    presidents_india[0] ='Pranab Mukherjee'
    presidents_india[1] ='Shankar Dayal Sharma'
    presidents_india[2] ='B.D.Jatti'
    presidents_india[3] ='Hidayatullah'
    presidents_india[4] ='Zakir Husain'
    presidents_india[5] ='Sarvepalli Radha Krishna'
    presidents_india[6] ='Neelam Sanjiva Reddy'
    presidents_india[7] ='K.R.Narayan'
    presidents_india[8] ='Varahagiri Venkata GIri'
    presidents_india[9] ='Giani Zail Singh'
    presidents_india[10]='Venkataraman'
    presidents_india[11]='Fakhruddin Ali Ahmed'
    presidents_india[12]='Rajendra Prasad'
    print("Updated Elemnts:",presidents_india)
    print("")   

# 5.Check the updated Elemensts.
def verifyupdatedelements():
    print("=======================================")
    print("Checking Updated Elements In The List")
    print("=======================================")
    print("")
    print("presidents Of india List After Updating Index 0  : ", presidents_india[0], end = "\n")
    print("presidents Of india List After Updating Index 1  : ", presidents_india[1], end = "\n")
    print("presidents Of india List After Updating Index 2  : ", presidents_india[2], end = "\n")
    print("presidents Of india List After Updating Index 3  : ", presidents_india[3], end = "\n")
    print("presidents Of india List After Updating Index 4  : ", presidents_india[4], end = "\n")
    print("presidents Of india List After Updating Index 5  : ", presidents_india[5], end = "\n")
    print("presidents Of india List After Updating Index 6  : ", presidents_india[6], end = "\n")
    print("presidents Of india List After Updating Index 7  : ", presidents_india[7], end = "\n")
    print("presidents Of india List After Updating Index 8  : ", presidents_india[8], end = "\n")
    print("presidents Of india List After Updating Index 9  : ", presidents_india[9], end = "\n")
    print("presidents Of india List After Updating Index 10 : ", presidents_india[10], end = "\n")
    print("presidents Of india List After Updating Index 11 : ", presidents_india[11], end = "\n")
    print("presidents Of india List After Updating Index 12 : ", presidents_india[12], end = "\n")
    print(" ")   

# 6.add new elements .

def add_new_elements():
    print("=======================================")
    print("Adding New Elements Into The List")
    print("=======================================")
    print("")
    presidents_india.append('Prathiba Devi singh Patil')
    presidents_india.append('Ram Nath Kovindh')
    print("Added New Elements In The List:",presidents_india)
    print(" ")

# 7.insert new elements at particular position.

def insert_new_items():
    print("========================================================")
    print("Insering New Elements Into The List Based On Positions")
    print("=========================================================")
    print(" ")
    presidents_india.insert(0,'Abdul Kalam')
    presidents_india.insert(10,'Draupadi Murmu')
    print("Inserted Elements:",presidents_india)
    print(" ")


# 8.Delete the element at particular position. 

def delete_element():
    print("========================================================")
    print("Deleting Elements In The List Based On Position")
    print("=========================================================")
    print(" ")
    print("Deleting element in the list at Index 3:",presidents_india.pop(3))
    print(" ")
    print(presidents_india)
    print(" ")    

# 9.access the element at particular position.  

def displaying_element():
    print("========================================================")
    print("Accessing Element In The List Based On Positions")
    print("=========================================================")
    print("presidents Of india List After Removing Element Index 0  : ", presidents_india[0], end = "\n")
    print("presidents Of india List After Removing Element Index 1  : ", presidents_india[1], end = "\n")
    print("presidents Of india List After Removing Element Index 2  : ", presidents_india[2], end = "\n")
    print("presidents Of india List After Removing Element Index 3  : ", presidents_india[3], end = "\n")
    print("presidents Of india List After Removing Element Index 4  : ", presidents_india[4], end = "\n")
    print("presidents Of india List After Removing Element Index 5  : ", presidents_india[5], end = "\n")
    print("presidents Of india List After Removing Element Index 6  : ", presidents_india[6], end = "\n")
    print("presidents Of india List After Removing Element Index 7  : ", presidents_india[7], end = "\n")
    print("presidents Of india List After Removing Element Index 8  : ", presidents_india[8], end = "\n")
    print("presidents Of india List After Removing Element Index 9  : ", presidents_india[9], end = "\n")
    print("presidents Of india List After Removing Element Index 10 : ", presidents_india[10], end = "\n")
    print("presidents Of india List After Removing Element Index 11 : ", presidents_india[11], end = "\n")
    print("presidents Of india List After Removing Element Index 12 : ", presidents_india[12], end = "\n")
    print("presidents Of india List After Removing Element Index 13 : ", presidents_india[13], end = "\n")
    print("presidents Of india List After Removing Element Index 14 : ", presidents_india[14], end = "\n")
    print("presidents of india List After Removing Element Index 15 : ", presidents_india[15], end = "\n")
    print(" ")


# 10.pop the element.
def pop_elememt():
    print("====================================")
    print("Removing Element In The List")
    print("====================================")
    print("")
    print("Removing element in the list At Index 8:",presidents_india.pop(8))
    print(" ")
    print("After Removing Elemnt:",presidents_india)













def main():
    createlist()
    generateitems()
    printitems()
    modifyingelements()
    verifyupdatedelements()
    add_new_elements()
    insert_new_items()
    delete_element()
    displaying_element()
    pop_elememt()



if __name__ == "__main__":
    main()
