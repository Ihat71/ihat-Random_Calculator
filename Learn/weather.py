import requests
API = '46ad3c754c2ebd172555b516643948ff'
lat = "36.1877"
lon = "44.0107"
cnt = "7"
url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}"


response = requests.get(url)

if response.status_code == 200:
    print("yo")
    print(response.headers['Content-Type'])
    data = response.json()
    print(data)
else:
    print("no")
    print(response.text)