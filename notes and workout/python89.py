import requests
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.status_code)
# print('-'*100)
# print(response.text)
# print('-'*100)
# print(response.content)
# print('-'*100)
# print(response.json())
# print('-'*100)
# print(response.headers)
# print('-'*100)
# print(response.url)
# print('-'*100)
# print(response.encoding)
# print("-"*100)
# print(response.raise_for_status())

# response= requests.get("https://google.com")
# text = response.text
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(text,"html.parser")
# print(soup.prettify())

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": "Learning Python",
#     "body": "I am learning the requests module.",
#     "userId": 1

# }
# response = requests.post(url, json=data)

# print(response.status_code)
# print(response.json())

response2 = requests.options("https://jsonplaceholder.typicode.com")
print(response2.status_code)
allowed_methods = response2.headers.get("access-control-allow-methods")
# print(allowed_methods)
# print("\nAll Response Headers:")
# for key, value in response2.headers.items():
#     print(f"{key}: {value}")
