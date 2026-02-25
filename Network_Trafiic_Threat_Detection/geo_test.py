import requests
ip="74.125.158.201"
response=requests.get(f"https://ipinfo.io/{ip}/json")
data=response.json()
print("IP Address:",ip)
print("Country:",data.get("country","Unknown"))
print("City:",data.get("city","Unknown"))