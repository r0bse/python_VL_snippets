import keyword

# dc_list=["Batman", "Superman", "Wonder Woman", "Flash", "Green Lantern"]
#
# list = list(range(10))
# print("start: 0, bis: 4, step: 1", list[0:4:1])
# print("start: 0, bis: default, step: default", list[0::])
# print("start: 1, bis: 8, step: 1", list[1:8:2])
# print("start: -1, bis: default, step: -2", list[-1::-2])
#
# for value in range(10):
#     print(value)
#
# for value in range(3, 10, 2):
#     print(value) # 3, 5, 7, 9

#
# for hero in dc_list:
#   print(hero)


# def useOfJavaPractice():
#     return "somethingSomething"
#
# marvel_tuple = ("Spider-Man", "Captain America", "Hulk", "Ant-Man", "Black Widow")
#
# if "Spider-Man" in marvel_tuple:
#   print("Spider-Man is in marvel_tuple")
#
# if "Spider-Man" not in dc_list:
#   print("Spider-Man is not in dc_list")


best_map = {"best_marvel":"Spider-Man", "best_dc":"Batman"}

# for best in best_map:
#   print(best, best_map[best])
#
# if "Spider-Man" in best_map:
#   print("Spider-Man is in best_map")

# best_set = ("Spider-Man", "Batman")
#
# for best in best_set:
#   print(best)
#
# best_set.index("asd")
# best_set.add("Superman")
# # copy=best_set.copy()
# # print("remove")
# # # best_set.remove()
# # print(best_set)
# # best_set.discard("asd")
# # print(best_set)
# print(best_set.intersection({"Spider-Man", "Batman"}))
# print(best_set)
# print(best_set.difference({"Spider-Man", "Batman"}))
# print(best_set)
# print(best_set.union({"asd"}))
# print(best_set)
# best_set.issubset()
# best_set.issuperset()

# best_copy = best_map.copy()
# best_copy.clear()
# print(best_map.get("best_marvel"))

# best_map.pop()
# print(best_map.items())
# print(best_map.keys())

best_map["myOpinion"] = "Squirrel Girl"
for best in best_map:
    print(best, best_map[best])

# best_map.