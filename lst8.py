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

def create_empty_list():
    print("========================")
    print("Creating Empty List")
    print("========================")
    global list_holidays
    list_holidays=[]
    print("Created List is:",list_holidays)
    print(" ")

# 2.Generate a Elements.
def generate_list():
    print("========================")
    print("Generating a List")
    print("========================")
    # list_holidays.append('Dasara')
    # list_holidays.append('Sankranthi')
    # list_holidays.append('Christmas')
    # list_holidays.append('Krishnastami')
    # list_holidays.append('Ugadi')
    # list_holidays.append('Diwali')
    # list_holidays.append('Onam')
    # list_holidays.append('Pongal')
    # list_holidays.append('Holi')
    # list_holidays.append('Ganesh Chathurthi')
    # list_holidays.append('Raksha Bandhan')
    # list_holidays.append('Holi')
    # list_holidays.append('Maha Shivarathri')
    # list_holidays.append('Gudi Padwa')

    list_holidays.extend(['Dasara', 'Sankranthi', 'Christmas', 'Krishnastami', 'Ugadi', 'Diwali', 'Onam', 'Pongal', 'Holi', 'Ganesh Chathurthi', 'Raksha Bandhan','Maha Shivarathri', 'Gudi Padwa'])
    
    print("Generated List is:",list_holidays)
    print(" ")

# 3.Access the Elements.

def access_items():
    print("===============================")
    print("Accessing elements in the list")
    print("===============================")
    print("In Holidays List Index 0  : ", list_holidays[0], end = "\n")
    print("In Holidays List Index 1  : ", list_holidays[1], end = "\n")
    print("In Holidays List Index 2  : ", list_holidays[2], end = "\n")
    print("In Holidays List Index 3  : ", list_holidays[3], end = "\n")
    print("In Holidays List Index 4  : ", list_holidays[4], end = "\n")
    print("In Holidays List Index 5  : ", list_holidays[5], end = "\n")
    print("In Holidays List Index 6  : ", list_holidays[6], end = "\n")
    print("In Holidays List Index 7  : ", list_holidays[7], end = "\n")
    print("In Holidays List Index 8  : ", list_holidays[8], end = "\n")
    print("In Holidays List Index 9  : ", list_holidays[9], end = "\n")
    print("In Holidays List Index 10 : ", list_holidays[10], end = "\n")
    print("In Holidays List Index 11 : ", list_holidays[11], end = "\n")
    print("In Holidays List Index 12 : ", list_holidays[12], end = "\n")
    print(" ")

# 4.Update the Elemensts.
def modifying_items():
    print("===============================")
    print("Updating elements in the list")
    print("===============================")
    list_holidays[0] ='Krishnastami'
    list_holidays[1] ='Diwali'
    list_holidays[2] ='Christmas'
    list_holidays[3] ='Dasara'
    list_holidays[4] ='Ganesh Chathurthi'
    list_holidays[5] ='Holi'
    list_holidays[6] ='Maha Shivarathri'
    list_holidays[7] ='Onam'
    list_holidays[8] ='Raksha Bandhan'
    list_holidays[9] ='Sankranthi'
    list_holidays[10]='Pongal'
    list_holidays[11]='Gudi Padwa'
    list_holidays[12]='Ugadi'
    print(list_holidays)
    print(" ")
   
# 5.Check the updated Elemensts.

def check_updated_elements():
    print("=======================================")
    print("Checking Updated Elements In The List")
    print("=======================================")
    print("Holidays List After Updating Index 0  : ", list_holidays[0], end = "\n")
    print("Holidays List After Updating Index 1  : ", list_holidays[1], end = "\n")
    print("Holidays List After Updating Index 2  : ", list_holidays[2], end = "\n")
    print("Holidays List After Updating Index 3  : ", list_holidays[3], end = "\n")
    print("Holidays List After Updating Index 4  : ", list_holidays[4], end = "\n")
    print("Holidays List After Updating Index 5  : ", list_holidays[5], end = "\n")
    print("Holidays List After Updating Index 6  : ", list_holidays[6], end = "\n")
    print("Holidays List After Updating Index 7  : ", list_holidays[7], end = "\n")
    print("Holidays List After Updating Index 8  : ", list_holidays[8], end = "\n")
    print("Holidays List After Updating Index 9  : ", list_holidays[9], end = "\n")
    print("Holidays List After Updating Index 10 : ", list_holidays[10], end = "\n")
    print("Holidays List After Updating Index 11 : ", list_holidays[11], end = "\n")
    print("Holidays List After Updating Index 12 : ", list_holidays[12], end = "\n")
    print(" ")

# 6.add new elements.
def add_new_elements():
    print("=======================================")
    print("Adding New Elements Into The List")
    print("=======================================")

    list_holidays.append('Independence Day')
    list_holidays.append('Republic Day')
    print("Added New Elements In The List:",list_holidays)
    print(" ")


# 7.insert new elements at particular position.

def insert_new_items():
    print("========================================================")
    print("Insering New Elements Into The List Based On Positions")
    print("=========================================================")
    list_holidays.insert(6,'Childrens Day')
    list_holidays.insert(9,'Gandhi Jayanthi')
    print("Inserted Elements:",list_holidays)
    print(" ")

# 8.Delete the element at particular position.

def remove_element():
    print("========================================================")
    print("Deleting Elements In The List Based On Position")
    print("=========================================================")
    print("Deleting element in the list at Index 12:",list_holidays.pop(12))
    print(" ")
    print(list_holidays)
    print(" ")

# 9.access the element at particular position.
def displaying_element():
    print("========================================================")
    print("Accessing Element In The List Based On Positions")
    print("=========================================================")
    print("")
    print("Holidays List After Removing Element Index 0  : ", list_holidays[0], end = "\n")
    print("Holidays List After Removing Element Index 1  : ", list_holidays[1], end = "\n")
    print("Holidays List After Removing Element Index 2  : ", list_holidays[2], end = "\n")
    print("Holidays List After Removing Element Index 3  : ", list_holidays[3], end = "\n")
    print("Holidays List After Removing Element Index 4  : ", list_holidays[4], end = "\n")
    print("Holidays List After Removing Element Index 5  : ", list_holidays[5], end = "\n")
    print("Holidays List After Removing Element Index 6  : ", list_holidays[6], end = "\n")
    print("Holidays List After Removing Element Index 7  : ", list_holidays[7], end = "\n")
    print("Holidays List After Removing Element Index 8  : ", list_holidays[8], end = "\n")
    print("Holidays List After Removing Element Index 9  : ", list_holidays[9], end = "\n")
    print("Holidays List After Removing Element Index 10 : ", list_holidays[10],end = "\n")
    print("Holidays List After Removing Element Index 11 : ", list_holidays[11],end = "\n")
    print("Holidays List After Removing Element Index 12 : ", list_holidays[12],end = "\n")
    print("Holidays List After Removing Element Index 13 : ", list_holidays[13],end = "\n")
    print("Holidays List After Removing Element Index 14 : ", list_holidays[14],end = "\n")
    print("Holidays List After Removing Element Index 15 : ", list_holidays[15],end = "\n")
    print(" ")


# 10.pop the element.
def pop_elememt():
    print("====================================")
    print("Removing Element In The List")
    print("====================================")
    print("Removing element in the list At Index 12:",list_holidays.pop(12))
    print(" ")
    print("After Removing Elemnt:",list_holidays)








        


























def main():
    #call the create_list()
   create_empty_list()
   generate_list()
   access_items()
   modifying_items()
   check_updated_elements()
   add_new_elements()
   insert_new_items()
   remove_element()
   displaying_element()
   pop_elememt()


if __name__ == "__main__":
    main()

 