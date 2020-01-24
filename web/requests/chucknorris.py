import json
import requests


def print_random_joke():
    response = requests.get("http://api.icndb.com/jokes/random")
    response_body = response.json() #parse response into json dictionary
    print("random chuck norris joke: ", response_body["value"]["joke"] )# access json dictionary field "text"


if __name__ == "__main__":
    print_random_joke()
    print_random_joke()
    print_random_joke()

