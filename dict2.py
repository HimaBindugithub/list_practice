#Assignment Employee Information

#1.Creating a dictionary with Employee Information

def creating_dictionary():
    print("=================================================")
    print("Creating the dictionary By Using Key:Value Pairs")
    print("=================================================")
    global dict_emp_info
    dict_emp_info={
        'emp_id'                 :   1,
        'emp_first_name'         :  'Gaddam',
        'emp_last_name'          :  'Bindu', 
        'emp_full_name'          :  'HimaBindu',
        'emp_age'                :   23,
        'emp_birth_date'         :   {"month":"June","Date":27,"Year":2000},
        'emp_gender'             :  'Female',
        'emp_marital_status'     :  "Single",
        'emp_blood_group'        :  "o+ve ",
        'emp_loc'                :  'Bangalore',
        'emp_company'            :  'TCS',
        'emp_salary'             :   30000,
        'emp_role'               :  'Developer',
        'emp_hire_date'          :  {"month":"January","Date":9,"Year":2022},
        'emp_phno'               :  [9182734562,6120345678],
        'emp_email'              :  "bindu@gmail.com", 
        'emp_professional_email' :  "bindu.hima@gmail.com",
        'emp_Hobbies'            :  ["travelling","Playing Shuttle","art"],
        'emp_talents'            :  "Dancing",
        'emp_nationality'        :  "Indian",
        'emp_city'               :  'Bangalore', 
        'emp_state'              :  'Karnataka',
        'emp_country'            :  'India',
        'emp_bank_name'          :  'SBI',
        'emp_bank_street_name'   :  'Gandhi nagar',
        'emp_Address'     :  {
               "Present   Add" : {"dno":6-90,"fname":"Bindu","street":"ashoknagar","city":"Bangalore","pincode":52345,"mobileno":6120345678},
               "Permanent Add" : {"dno":6-90,"fname":"Bindu","street":"ashoknagar","city":"Bangalore","pincode":52345,"mobileno":6120345678}
                }
        }
    print("Created dictionary is:",dict_emp_info)
    print("")      

#2.Accessing values using keys

def accessing_values():
    print("================================================")
    print("Accessing the dictionary values by using keys")
    print("================================================")  
    print(dict_emp_info['emp_id'])
    print(dict_emp_info['emp_first_name'])
    print(dict_emp_info['emp_last_name'])
    print(dict_emp_info['emp_full_name'])
    print(dict_emp_info['emp_age'])
    print(dict_emp_info['emp_birth_date'])
    print(dict_emp_info['emp_gender'])
    print(dict_emp_info['emp_marital_status'])
    print(dict_emp_info['emp_blood_group'])
    print(dict_emp_info['emp_loc'])
    print(dict_emp_info['emp_company'])
    print(dict_emp_info['emp_salary'])
    print(dict_emp_info['emp_role'])
    print(dict_emp_info['emp_hire_date'])
    print(dict_emp_info['emp_phno'])
    print(dict_emp_info['emp_email'])
    print(dict_emp_info['emp_Hobbies'])
    print(dict_emp_info['emp_nationality'])
    print(dict_emp_info['emp_city'])
    print(dict_emp_info['emp_state'])
    print(dict_emp_info['emp_country'])
    print(dict_emp_info['emp_bank_name'])
    print(dict_emp_info['emp_bank_street_name'])
    print(dict_emp_info['emp_Address'])
    print("")

    #3.Iterating through keys and values Using For Loop

    print("=============================================")
    print("Accessing the Values by using For Loop ")
    print("=============================================")
    for i,j in dict_emp_info.items():
        print(i,":",j)    
        print("")
#4.Updating values with Keys

def updating_values():
    print("================================================")
    print("Modifying the Dictionary Values By Using Keys")
    print("================================================")
    dict_emp_info['emp_company']='Google'
    dict_emp_info['emp_Hobbies']=['reading','Painting']
    print("After Updating Values in Dictionary:",dict_emp_info)
    print("")

#5.Adding new key:value pairs 

def adding_new_key_value():
    print("================================================")
    print("Adding new key,value pairs into the dictionary")
    print("================================================")    
    print("")
    print("Adding new key,value pairs into the dictionary")
    dict_emp_info['emp_work_experience']='2 years'
    print(dict_emp_info)
    print("")

#Deleting a key-value pair by using del

def deleting_value():
    print("=================================================")
    print("Deleting value in the dictionary based on key")
    print("=================================================")
    print("")
    del dict_emp_info['emp_bank_street_name']  
    print("After Deleting value in the dictionary :",dict_emp_info)
    print(" ")




def main():
    creating_dictionary()
    accessing_values()
    updating_values()
    adding_new_key_value()
    deleting_value()

if "__main__"==__name__:
    main()    