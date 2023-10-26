# Write a program that asks the user to enter a list of at least five integers. Do the following:
# (a) Print out the total number of items in the list.
# (b) Print out the fourth item (index 3) in the list.
# (c) Print out the last three items in the list.
# (d) Print out all the items in the list except the first two.
# (e) Print out the list in reverse order.
# (f) Print out the largest and smallest values in the list.
# (g) Print out the sum of all the values in the list.
# (h) If the list contains a zero, print out the index of the first zero in the list, and otherwise print out
# a message saying there are no zeroes.
# (i) Sort the list and print out the list after sorting.
# (j) Delete the first item from the (now sorted) list and print out the new list.
# (k) Change the second-to-last item in the list to 9876 and print out the new list.
# (l) Append the value -500 to the end of the list and print out the new list


# (a) Print out the total number of items in the list.
def total_number_of_items():
    print("===================================")
    print("Total number of items in the list")
    print("===================================")
    global list 
    list=[9,1,0,2,8]
    print("Total number of items in the list:",len(list))

# (b) Print out the fourth item (index 3) in the list.
def access_list():
    print("===================================")
    print("Accesing items in the list")
    print("===================================")
    print("Accesing items in the list:",list.index(2))

# (c) Print out the last three items in the list.
def Fetching_list():
    print("===================================")
    print("Fetching items in the list")
    print("===================================")
    print("Fetching last three items in the list:",list[2:])

# (d) Print out all the items in the list except the first two.
def displaying_list():
    print("===================================")
    print("Displaying items in the list")
    print("===================================")
    print("Fetching last three items in the list:",list[2:])

# (e) Print out the list in reverse order.
def reverse_list():
    print("===================================")
    print("Reversing items in the list")
    print("===================================")
    # print("Printing the list in the reverse order:",list.reverse())
    list.reverse()
    print(list)

# (f) Print out the largest and smallest values in the list.

def largest_value():
    print("===================================")
    print("Largest value in the list")
    print("===================================")
    print("Printing largest value in the list:",max(list))

def smallest_value():
    print("===================================")
    print("smallest value in the list")
    print("===================================")
    print("Printing smallest value in the list:",min(list))

# (g) Print out the sum of all the values in the list.

def sum_list():
    print("===================================")
    print("Adding values in the list")
    print("===================================")
    print("Printing Adding all values in the list:",sum(list))
 
# (h) If the list contains a zero, print out the index of the first zero in the list, and otherwise print out
# a message saying there are no zeroes.
def print_index():
    print("===================================")
    print("Printing index values in the list")
    print("===================================")
    print("Printing index of the first zero in the list:",list.index(0))

# (i) Sort the list and print out the list after sorting.

def sort_list():
    print("===================================")
    print("Sorting values in the list")
    print("===================================")
    print(list.sort())
    print(list)

# (j) Delete the first item from the (now sorted) list and print out the new list.

def remove_item():
    print("===================================")
    print("Sorting values in the list")
    print("===================================")
    list.pop(0)
    print(list)

# (k) Change the second-to-last item in the list to 9876 and print out the new list.

def modifying_list():
    print("===================================")
    print("Updating values in the list")
    print("===================================")
    list.append(3)
    list.append(4)
    list[2]=9
    list[3]=8
    list[4]=7
    list[5]=6
    print(list)

# (l) Append the value -500 to the end of the list and print out the new list    
def append_item():
    print("===================================")
    print("Adding item at the end of list")
    print("===================================")
    print(list.append(500))
    print(list)


def main():
     
    total_number_of_items()
    access_list()
    Fetching_list()
    displaying_list()
    reverse_list()
    largest_value()
    smallest_value()
    sum_list()
    print_index()
    sort_list()
    remove_item()
    modifying_list()
    append_item()
    
if __name__ == "__main__":
    main()
