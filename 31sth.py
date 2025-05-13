# Global variable
global_var = 10

def modify_global():
    global global_var  
    global_var = global_var + 5
    print("Inside function, global_var:", global_var)

modify_global()

print("Outside function, global_var:", global_var)
