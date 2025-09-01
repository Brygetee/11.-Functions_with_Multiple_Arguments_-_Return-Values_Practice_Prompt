"""
11. Functions with Multiple Arguments & Return Values
What you should know: Pass multiple inputs into a function and return more than one value.
Practice Prompt: Write a function that takes project name + fabric type and returns two
values: estimated fabric yards and recommended needle size.
"""
"""------------------Initial Code--------------------------"""
# def project_helper(name, fabric):
#     #pick needle size according to fabric
#     if fabric == "heavyweight":
#         needle_size = "16/100"
#     elif fabric == "medium":
#         needle_size = "14/90"
#     elif fabric == "lightweight":
#         needle_size = "11/75"
#     else:
#         print("Pick a valid fabric weight.")
#     if name == "blouse":
#         yards = 1.5
#     elif name == "dress":
#         yards = 3
#     elif name == "pants":
#         yards = 4
#     else:
#         print("Pick a valid project.")
#     print(f"You will be making a {fabric} weight {name} that requires {needle_size} size needles and {yards} yards of fabric.")
#
# fabric_weight = input("What type of fabric weight will you be working with, heavyweight, medium or lightweight fabric?").lower()
# project_name = input("What type of project will you be working on, blouse, dress, or pants?")
# project_helper(project_name, fabric_weight)

"""---------------------How to improve code-----------------------------
1.Code doesn't return anything, must return not print.
2.If the input is invalid, needle_size or yards might never be assigned.
3.Remove excessive if statements a dictionary lookup is more concise
4.function should focus on logic (calculating/returning values). 
The print should happen outside the function for clarity
"""

#create dictionaries within the function
def project_helper(name, fabric):
    fabric_needles = {
        "heavyweight": "16/100",
        "medium": "14/90",
        "lightweight": "11/75"
    }
    project_yards = {
        "blouse": 1.5,
        "dress": 3,
        "pants": 4
    }
    needle_size = fabric_needles.get(fabric)
    yards = project_yards.get(name)


    if needle_size is None or yards is None:
        return None, None

    return yards, needle_size



fabric_weight = input("What type of fabric weight will you be working with?(heavyweight, medium, lightweight): ").lower()
project_name = input("What type of project will you be working on? (blouse, dress, pants): ").lower()

yards, needle_size = project_helper(name=project_name, fabric=fabric_weight)

if yards and needle_size:
    print(f"You will be making a {fabric_weight} {project_name} "
          f"that requires {needle_size} needles and {yards} yards of fabric.")
else:
    print("Invalid input. Please try again.")