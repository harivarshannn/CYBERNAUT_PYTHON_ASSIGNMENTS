def set1():
     set1 = set(input("Enter elements of the first set: ").split())
     set2 = set(input("Enter elements of the second set: ").split())

     common_elements = set1.intersection(set2)

     if common_elements:
           print(f"The common elements are: {common_elements}")
     else:
          print("There are no common elements.")
def string1():
   
        text = "Cybernaut is learning platform."


        text_with_underscores = text.replace(" ", "_")
        print(f"String with underscores: {text_with_underscores}")

        # Remove spaces entirely
        text_no_spaces = text.replace(" ", "")
        print(f"String without spaces: {text_no_spaces}")


set1()
string1()

