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


# 1.Create a Empty List.
def create_list():
    print("=======================")
    print("Creating An Empty List")
    print("=======================")
    global women_entrepreneurs
    women_entrepreneurs=[]
    print("")
    print("Created An Empty List:",women_entrepreneurs)
    print("")

# 2.Generate a Elements.

def generate_items():
    print("====================================")
    print("Generating An Items Into The  List")
    print("====================================")
    print("")
    women_entrepreneurs.extend(['Aditi Gupta','Chitra Gurnani Daga','Falguni Nayar','Garima Satija','Harpreet Kaur','Pranshu Bhandari','Radhika Ghai Aggarwal','Shradha Sharma','Upasana Taku','Ankita Gaba','Richa Kar','Suchi Mukherjee','Swati Bhargave'])
    print("Generated List:",women_entrepreneurs)
    print("")

# 3.Access the Elements.
def print_items():
    print("====================================")
    print("Accessing Items From The  List")
    print("====================================")
    print("")
    print("In Women Entrepreneurs List Index 0 :",women_entrepreneurs[0],end="\n")
    print("In Women Entrepreneurs List Index 1 :",women_entrepreneurs[1],end="\n")
    print("In Women Entrepreneurs List Index 2 :",women_entrepreneurs[2],end="\n")
    print("In Women Entrepreneurs List Index 3 :",women_entrepreneurs[3],end="\n")
    print("In Women Entrepreneurs List Index 4 :",women_entrepreneurs[4],end="\n")
    print("In Women Entrepreneurs List Index 5 :",women_entrepreneurs[5],end="\n")
    print("In Women Entrepreneurs List Index 6 :",women_entrepreneurs[6],end="\n")
    print("In Women Entrepreneurs List Index 7 :",women_entrepreneurs[7],end="\n")
    print("In Women Entrepreneurs List Index 8 :",women_entrepreneurs[8],end="\n")
    print("In Women Entrepreneurs List Index 9 :",women_entrepreneurs[9],end="\n")
    print("In Women Entrepreneurs List Index 10:",women_entrepreneurs[10],end="\n")
    print("In Women Entrepreneurs List Index 11:",women_entrepreneurs[11],end="\n")
    print("In Women Entrepreneurs List Index 12:",women_entrepreneurs[12],end="\n")
    print(" ")

# 4.Update the Elemensts.

def modifying_elements():
    print("====================================")
    print("Updating Elements In The  List")
    print("====================================")
    print("")
    women_entrepreneurs[0] ='Garima Satija'
    women_entrepreneurs[1] ='Pranshu Bhandari'
    women_entrepreneurs[2] ='Aditi Gupta'
    women_entrepreneurs[3] ='Harpreet Kaur'
    women_entrepreneurs[4] ='Swati Bhargave'
    women_entrepreneurs[5] ='Radhika Ghai Aggarwal'
    women_entrepreneurs[6] ='Upasana Taku'
    women_entrepreneurs[7] ='Chitra Gurnani Daga'
    women_entrepreneurs[8] ='Shradha Sharma'
    women_entrepreneurs[9] ='Falguni Nayar'
    women_entrepreneurs[10]='Ankita Gaba'
    women_entrepreneurs[11]='Suchi Mukherjee'
    women_entrepreneurs[12]='Richa Kar'
    print("Updated Elemnts:",women_entrepreneurs)
    print("")

# 5.Check the updated Elemensts.
def verify_updated_elements():
    print("=======================================")
    print("Checking Updated Elements In The List")
    print("=======================================")
    print("")
    print("women_entrepreneurs List After Updating Index 0  : ", women_entrepreneurs[0], end = "\n")
    print("women_entrepreneurs List After Updating Index 1  : ", women_entrepreneurs[1], end = "\n")
    print("women_entrepreneurs List After Updating Index 2  : ", women_entrepreneurs[2], end = "\n")
    print("women_entrepreneurs List After Updating Index 3  : ", women_entrepreneurs[3], end = "\n")
    print("women_entrepreneurs List After Updating Index 4  : ", women_entrepreneurs[4], end = "\n")
    print("women_entrepreneurs List After Updating Index 5  : ", women_entrepreneurs[5], end = "\n")
    print("women_entrepreneurs List After Updating Index 6  : ", women_entrepreneurs[6], end = "\n")
    print("women_entrepreneurs List After Updating Index 7  : ", women_entrepreneurs[7], end = "\n")
    print("women_entrepreneurs List After Updating Index 8  : ", women_entrepreneurs[8], end = "\n")
    print("women_entrepreneurs List After Updating Index 9  : ", women_entrepreneurs[9], end = "\n")
    print("women_entrepreneurs List After Updating Index 10 : ", women_entrepreneurs[10], end = "\n")
    print("women_entrepreneurs List After Updating Index 11 : ", women_entrepreneurs[11], end = "\n")
    print("women_entrepreneurs List After Updating Index 12 : ", women_entrepreneurs[12], end = "\n")
    print(" ")


# 6.add new elements .

def add_new_elements():
    print("=======================================")
    print("Adding New Elements Into The List")
    print("=======================================")
    print("")
    women_entrepreneurs.append('Zeenia Percy Master')
    women_entrepreneurs.append('Sabina Chopra')
    print("Added New Elements In The List:",women_entrepreneurs)
    print(" ")


# 7.insert new elements at particular position.

def insert_new_items():
    print("========================================================")
    print("Insering New Elements Into The List Based On Positions")
    print("=========================================================")
    print(" ")
    women_entrepreneurs.insert(5,'Ashwini Asokan')
    women_entrepreneurs.insert(10,'Debadutta Upadhyaya')
    print("Inserted Elements:",women_entrepreneurs)
    print(" ")

# 8.Delete the element at particular position. 

def delete_element():
    print("========================================================")
    print("Deleting Elements In The List Based On Position")
    print("=========================================================")
    print(" ")
    print("Deleting element in the list at Index 3:",women_entrepreneurs.pop(3))
    print(" ")
    print(women_entrepreneurs)
    print(" ")

# 9.access the element at particular position.  

def displaying_element():
    print("========================================================")
    print("Accessing Element In The List Based On Positions")
    print("=========================================================")
    print("women_entrepreneurs List After Removing Element Index 0  : ", women_entrepreneurs[0], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 1  : ", women_entrepreneurs[1], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 2  : ", women_entrepreneurs[2], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 3  : ", women_entrepreneurs[3], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 4  : ", women_entrepreneurs[4], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 5  : ", women_entrepreneurs[5], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 6  : ", women_entrepreneurs[6], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 7  : ", women_entrepreneurs[7], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 8  : ", women_entrepreneurs[8], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 9  : ", women_entrepreneurs[9], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 10 : ", women_entrepreneurs[10], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 11 : ", women_entrepreneurs[11], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 12 : ", women_entrepreneurs[12], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 13 : ", women_entrepreneurs[13], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 14 : ", women_entrepreneurs[14], end = "\n")
    print("women_entrepreneurs List After Removing Element Index 15 : ", women_entrepreneurs[15], end = "\n")
    print(" ")

# 10.pop the element.
def pop_elememt():
    print("====================================")
    print("Removing Element In The List")
    print("====================================")
    print("")
    print("Removing element in the list At Index 8:",women_entrepreneurs.pop(8))
    print(" ")
    print("After Removing Elemnt:",women_entrepreneurs)






def main():
    create_list()
    generate_items()
    print_items()
    modifying_elements()
    verify_updated_elements()
    add_new_elements()
    insert_new_items()
    delete_element()
    displaying_element()
    pop_elememt()



if __name__ == "__main__":
    main()