from copy import deepcopy
from vl1.shallow_copy.Dto import Dto

original_list=[Dto("element 1"), Dto("element 2"), Dto("element 3")]
print("The original_list before:  {0}".format(original_list))

deep_copy = deepcopy(original_list)
deep_copy[0].string = "changed value"
deep_copy.append(Dto("added element"))

print("The original_list: {0}".format(original_list))
print("The copied_list:   {0}".format(deep_copy))

print("The deep copied lists are the same: {0}"
      .format(id(original_list)==id(deep_copy)))
print("The deep copied objects are the same: {0}"
      .format(id(original_list[0])==id(deep_copy[0])))


