import requests 
def digitalocean_status():
    digitalocean_status = requests.get('https://status.digitalocean.com/api/v2/summary.json')
    status_r = digitalocean_status.json()
    result = status_r['status']['description']
    return result
print(digitalocean_status())