#make a project to scrape the web for urls concurrently
import concurrent.futures
import requests
import re
import time
urls = [
'https://plus.unsplash.com/premium_photo-1661878265739-da90bc1af051?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZWxlY3Ryb25pY3xlbnwwfHwwfHx8MA%3D%3D',
'https://plus.unsplash.com/premium_photo-1683120974913-1ef17fdec2a8?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGVsZWN0cm9uaWN8ZW58MHx8MHx8fDA%3D'
]

def get_url(url):
    r = requests.get(url)
    if r.status_code == 200:
        x = re.search(r'[-]{1}([0-9]*)[-]{1}', url)
        y = x.group(1) + '.jpg'
        with open(y, 'wb') as file:
            file.write(r.content)
        print('Downloaded! ')
    else:
        print(f'NO, you recieved a {r.status_code} error')

def main():
    with concurrent.futures.ThreadPoolExecutor(2) as executor:
        Futures = [executor.submit(get_url, url) for url in urls]
        for results in Futures:
            result = results.result()
            
            
        
main()

    


