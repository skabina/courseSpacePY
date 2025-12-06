import requests

site = 'https://jsonplaceholder.typicode.com/posts'


print("<------- GET REQUESTS -------->")

response_get = requests.get(url=site + '/1')

# print(response_get.text)
print(response_get.json())
# print(response_get.json()["title"])
# print(response_get.headers) # Data requests

# for a, b in response_get.headers.items():
#    print(f"{a}, --> {b}")

print("____________")
print(f"Status code: {response_get.status_code}")
print(response_get.reason)


print("<-------- POST REQUESTS -------->")

data = {
    'userId': 100,
}

response_post = requests.post(url=site, data=data)

print(response_post.text)
print("____________") 
print(f"Status code: {response_post.status_code}")
print(response_post.reason)

 
print("<------- PUT REQUESTS -------->")


data1 = {
    'userId': 10,
    'id': 67
}

response_put = requests.put(url=site + '/1', data=data1)

print(response_put.text)
print("_____________________")
print(f"Status code: {response_put.status_code}")
print(response_post.reason)


print("<------- DELETE REQUESTS -------->")

response_delete = requests.delete(url=site + '/1')


print(response_delete.text)
print("____________") 
print(f"Status code: {response_delete.status_code}")
print(response_delete.reason)
