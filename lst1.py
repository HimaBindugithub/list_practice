def create_list():
    print("========================")
    print("Creating the List")
    print("========================")
    global listsports
    listsports = ['Cricket', 'Foot Ball', 'Shuttle', 'Base Ball']
def access_list():      
    print("Accessing the List elements by using Indexing")
    print("In Sports List Index 0 : ", listsports[0], end = "\n")
    print("In Sports List Index 1 : ", listsports[1], end = "\n")
    print("In Sports List Index 2 : ", listsports[2], end = "\n")
    print("In Sports List Index 3 : ", listsports[3], end = "\n")


#call the create_list()
create_list()
access_list()
