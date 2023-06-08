


#------------------------------
#------- Built In Function 4 => Map -------
#--------------------------------
# [1] Map Take a Function + Iterator
# [2] Map called Map because It Map The Function on every Element
# [3] The Function can be Pre-defined Functin or Lambda Functio
#--------------------------------

# Use Map with Predefined Function
# # one Way

def formatText(text) :
    return f"- {text.strip().capitalize()} -"

myTexts = ["Salar" , "Raman" , "Gamel" , "Shergo"]

myFormatedData = map(formatText , myTexts) 

print(myFormatedData) # <map object at 0x00000274C353AC50>

for name in myFormatedData  :

    print(name)

# - Salar -
# - Raman -
# - Gamel -
# - Shergo -

print("-" * 50) # --------------------------------------------------

# two way 

def formatText(text) :
    return f"- {text.stript().capitalize()} -"

myTexts = ["Salar" , "Raman" , "Gamel" , "Shergo"]

print(myFormatedData) # <map object at 0x00000274C353AC50>

for name in map(formatText , myTexts):

    print(name)

# - Salar -
# - Raman -
# - Gamel -
# - Shergo -


print("-" * 50) # --------------------------------------------------

# Use Map with lambda Function


# def formatText(text) :
#     # return f"- {text.strip().capitalize()} -"

myTexts = ["Salar" , "Raman" , "Gamel" , "Shergo"]


for name in map(   lambda text : f"- {text.strip().capitalize()} -" , myTexts)  :

    print(name)

 # - Salar -
# - Raman -
# - Gamel -
# - Shergo -