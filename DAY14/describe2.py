def print_data(data):
    try:
        length = len(data)
        print(f"The length of {data} is {length}")
    except TypeError:
        print(f"The value {data} does not support length.")


print_data("rcb")     
print_data([1, 2, 3])   
print_data((1, 2, 3, 4)) 
print_data(42)          
