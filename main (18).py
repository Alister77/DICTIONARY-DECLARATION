programming_dictionary={
"bug": "An error in the program that prevents the program from running as expected",
"function": "A piece of code that easy call over and over again",
"loop" : "the action of doing something over and over again"
}

#retrieving items from dictionary
#print(programming_dictionary["function"])

#adding new item to  dictionary
programming_dictionary["loop"] = "the action of doing something over and over again"

#create an empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
programming_dictionary = {}
#print(empty_dictionary)

#edit an item in dictionary
programming_dictionary["bug"] = "A moth in your computer "
#print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

#nesting dictionary in dictionary
travel_log = {
  "mysore": {"visited_places":["palace","zoo","forum"],"total_visited":3},
  "avengers": {"fav_aven": [thor,captain,doctor], "total_aven":3},
}

#nesting dictionary in list
travel_log =[
  {
  "state": "mysore",
  "visited_places":["palace","zoo","forum"],
  "total_visited":3
  },
  {
  "marvels":"avengers",
  "fav_aven": [thor,captain,doctor],
  "total_aven":3
  },
]  
