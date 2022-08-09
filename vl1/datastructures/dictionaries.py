
empty_dictionary={}
empty_dictionary[0]="any value"
empty_dictionary["0"]=1234 # not a good idea!
empty_dictionary[1]="is allowed"

print(empty_dictionary) # Output: {0: 'any value', '0': 1234, 1: 'is allowed'}

dictionary={"key1":"value1", "key2":"value2"}
print(dictionary) #  Output: {'key1': 'value1', 'key2': 'value2'}

# iterating over a dictionary returns the key
for key in dictionary:
    print(key) # Output: key1 und key2
    print(dictionary[key]) # Output: value1 und value2