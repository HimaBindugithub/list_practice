#Assignment Person Information

#1.Creating a dictionary with Person Information 

def creating_dictionary():
    print("=================================================")
    print("Creating the dictionary By Using Key:Value Pairs")
    print("=================================================")
    global dict_person_info
    dict_person_info={
        'per_first_name'         :  'Ramisetty',
        'per_last_name'          :  'Mahitha', 
        'per_full_name'          :  'Ramisetty Mahitha',
        'per_age'                :   23,
        'per_birth_date'         :   {"month":"october","Date":14,"Year":1998},
        'per_education'          :   'BTech',
        'per_occupation'         :   'Interior Designer',
        'per_goal'               :   'Famous Interior Designer',
        'per_gender'             :   'Female',
        'per_marital_status'     :   "Single",
        'per_blood_group'        :   "A+ve ",
        'per_loc'                :   'Hyderabad',
        'per_prefered_language'  :   ['Telugu','English'],
        'per_mobile_no'          :   [9182734562,6120345678],
        'per_email'              :   "Mahitha1@gmail.com", 
        'per_Hobbies'            :   ["Reading","Designing"],
        'per_nationality'        :   "Indian",
        'per_city'               :   'Banjara Hills', 
        'per_state'              :   'Hyderabad',
        'per_country'            :   'India',
        'per_talents'            :   'Dancing', 
        'per_fav_color'          :   'Black', 
        'per_Address'     :  {
               "Present   Add" : {"dno":6-4,"fname":"Mahitha","street":"ashoknagar","city":"Hyderabad","pincode":52345,"mobileno":6120345678},
               "Permanent Add" : {"dno":6-4,"fname":"Mahitha","street":"ashoknagar","city":"Hyderabad","pincode":52345,"mobileno":6120345678}
                }
        }
    print("Created dictionary is:""\n",dict_person_info)
    print("")      

#2.Accessing values using keys

def accessing_values():
    print("================================================")
    print("Accessing the dictionary values by using keys")
    print("================================================")  
    print(dict_person_info['per_first_name'])
    print(dict_person_info['per_last_name'])
    print(dict_person_info['per_full_name'])
    print(dict_person_info['per_age'])
    print(dict_person_info['per_birth_date'])
    print(dict_person_info['per_gender'])
    print(dict_person_info['per_marital_status'])
    print(dict_person_info['per_blood_group'])
    print(dict_person_info['per_loc'])
    print(dict_person_info['per_mobile_no'])
    print(dict_person_info['per_email'])
    print(dict_person_info['per_Hobbies'])
    print(dict_person_info['per_nationality'])
    print(dict_person_info['per_city'])
    print(dict_person_info['per_state'])
    print(dict_person_info['per_country'])
    print(dict_person_info['per_education'])
    print(dict_person_info['per_occupation'])
    print(dict_person_info['per_Address'])
    print(dict_person_info['per_prefered_language'])
    print(dict_person_info['per_talents'])
    print(dict_person_info['per_goal'])
    print(dict_person_info['per_fav_color'])
    print(dict_person_info['per_talents'])
    print("")

    #3.Iterating through keys and values Using For Loop

    print("=============================================")
    print("Accessing the Values by using For Loop ")
    print("=============================================")
    for x,y in dict_person_info.items():
        print(x,":",y)    
        print("")
        
#4.Updating values with Keys

def updating_values():
    print("================================================")
    print("Modifying the Dictionary Values By Using Keys")
    print("================================================")
    dict_person_info['per_fav_color']='White'
    print("After Updating Values in Dictionary:""\n",dict_person_info)
    print("")

#5.Adding new key:value pairs 

def adding_new_key_value():
    print("================================================")
    print("Adding new key,value pairs into the dictionary")
    print("================================================")    
    print("")
    dict_person_info['per_fav_food']='Biryani'
    print("After Adding New Key:Value Pair into the dict_person_info:""\n",dict_person_info)
    print("")

#Deleting a key-value pair by using del

def Removing_value():
    print("=================================================")
    print("Deleting value in the dictionary based on key")
    print("=================================================")
    print("")
    del dict_person_info['per_marital_status']  
    print("After Deleting value in the dictionary :""\n",dict_person_info)
    print(" ")




def main():
    creating_dictionary()
    accessing_values()
    updating_values()
    adding_new_key_value()
    Removing_value()

if "__main__"==__name__:
    main()    


     