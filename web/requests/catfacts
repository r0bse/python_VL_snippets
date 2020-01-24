import json
import requests


def print_random_fact(animal_type:str):
    response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type="+animal_type+"&amount=1")
    response_body = response.json() #parse response into json dictionary
    print("random fact for ", animal_type, "is: \n", response_body["text"] )# access json dictionary field "text"


if __name__ == "__main__":
    print_random_fact("cat")
    print_random_fact("dog")
    print_random_fact("horse")

