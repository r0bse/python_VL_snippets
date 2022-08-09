from vl1.shallow_copy.Dto import Dto

original_list=[Dto("element 1"), Dto("element 2"), Dto("element 3")]
print("The original_list before:  {0}".format(original_list))

shallow_copy = original_list.copy()
shallow_copy[0].string = "changed value"
shallow_copy.append(Dto("added element"))

print("The original_list:         {0}".format(original_list))
print("The shallow copied_list:   {0}".format(shallow_copy))

print("The shallow copied lists are the same:   {0}"
      .format(id(original_list)==id(shallow_copy)))
print("The shallow copied objects are the same: {0}"
      .format(id(original_list[0])==id(shallow_copy[0])))

