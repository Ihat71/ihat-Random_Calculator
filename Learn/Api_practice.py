import requests

x = input('Enter your city name or lat and long information in this form: lat,long. ')

param = {
    'key':'e872f19aad18480b88994727242108',
    'q':f'{x}'
}
url = 'http://api.weatherapi.com/v1/current.json'
r = requests.get(url, params=param)

weather = r.json()
print(weather)

country = weather['location']['country']
city = weather['location']['region']
temp = str(weather['current']['temp_c']) + ' C'
localtime = weather['location']['localtime']
humidity = weather['current']['humidity']
feelslike_temp = str(weather['current']['feelslike_c']) + ' C'
clouds = weather['current']['cloud']
condition = weather['current']['condition']['text']



