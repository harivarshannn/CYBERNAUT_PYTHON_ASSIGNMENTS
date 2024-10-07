def set1():
     set1 = set(input("Enter elements of the first set: ").split())
     set2 = set(input("Enter elements of the second set: ").split())

     common_elements = set1.intersection(set2)

     if common_elements:
           print(f"The common elements are: {common_elements}")
     else:
          print("There are no common elements.")

set1()