import requests

f = open("list.txt", "r")


adminpanel= '/admin'

content = f.readlines()

for response in content:
    try:

        response = requests.get(f'{response}{adminpanel}')
        print(response.url, response)
    except requests.exceptions.ConnectionError as errc:

        print("Error Connecting:", errc)








