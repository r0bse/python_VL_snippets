from vl1.shallow_copy.Dto import Dto

original_list=[Dto("element 1"), Dto("element 2"), Dto("element 3")]
print("The original_list before:  {0}".format(original_list))

copied_list=original_list
copied_list[0].string = "changed value"
copied_list.append(Dto("added value"))

print("The original_list: {0}".format(original_list))
print("The copied_list:   {0}".format(copied_list))

print("The copied lists are having the same reference:   {0}"
      .format(id(original_list)==id(copied_list)))
print("The copied objects are having the same reference: {0}"
      .format(id(original_list[0])==id(copied_list[0])))

dto = Dto("irgend ein String")

print(dto)