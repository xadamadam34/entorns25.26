import requests

url = "https://api.chucknorris.io/jokes/random?category=food"
response = requests.get(url)
if response.status_code == 200:
    print("✅ Èxit!")
    print(response.text)
else:
    print(f"❌ Error {response.status_code}")