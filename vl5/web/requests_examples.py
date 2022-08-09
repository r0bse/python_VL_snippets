import requests

def get_request():
    r = requests.get('https://api.github.com/users/r0bse/events')
    json = r.json()
    print(json)


#get_request()


def all_requests():
    r = requests.post("http://httpbin.org/post")
    r = requests.put("http://httpbin.org/put")
    r = requests.delete("http://httpbin.org/delete")
    r = requests.head("http://httpbin.org/get")
    r = requests.options("http://httpbin.org/get")


def get_with_params():
    payload = {'schluessel1': 'wert1', 'schluessel2': 'wert2'}
    r = requests.get("http://httpbin.org/get", params=payload)

    print(r.url)

def perform_complex_post_request():
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://httpbin.org/post", data=payload)
    print(r.text)

# perform_complex_post_request()

def perform_post_request_with_string():
    import json
    url = 'https://api.github.com/some/endpoint' # 404 !
    payload = {'some': 'data'}

    r = requests.post(url, data=json.dumps(payload))
    print(r.text)

#perform_post_request_with_string()
def request_with_timout():
    requests.get('http://github.com', timeout=0.001)

request_with_timout()