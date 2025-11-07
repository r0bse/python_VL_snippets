import string
import math
import textwrap

def create_matrix(scope: str):
    doublescope= scope+scope
    i=0

    # erstellen der Matrize um die verschlüsselten Zeichen auszulesen
    matrix = {}
    for outer_char in scope:
        line = ""
        if i>len(scope):
            i=0
        k=0
        matrix[outer_char] = {}
        for inner_char in scope:
            matrix[outer_char][inner_char] = doublescope[i+k]
            line = line+doublescope[i+k]
            k=k+1

        # if i==0:
        #     print("   "+line) # header
        #     print("   "+"_"*len(line))
        # print(outer_char+": "+line)
        i=i+1
    return matrix

def calculate_key(input: str, inserted_key: str):

    # ermittlung des Multiplikators f.d. Key
    multiplier=math.ceil(len(input)/len(inserted_key))
    # ermittlung des Keys durch Multiplikation und anschließendem Slice des Strings
    key= (inserted_key*multiplier)[:len(input)]
    return key

def encrypt_vignere(matrix: dict, input: str, key: str) -> str:

    i=0
    result = ""
    for char in input:
        key_char = key[i]
        encrypted_char = matrix[char][key_char]
        result = result+encrypted_char
    return result

if __name__ == "__main__":

    scope = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

    input="abc"
    inserted_key="cab"

    matrix = create_matrix("abcde")
    key = calculate_key(input, inserted_key)
    result = encrypt_vignere(matrix, input, key)
    print("result:" + result)