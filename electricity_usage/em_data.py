import requests
import json

#query verwendet den angegebenen zonekey, 
#falls kein zonekey angegeben ist wird automatisch der zonekey der IP adresse verwendet  
url = "https://api-access.electricitymaps.com/free-tier/power-breakdown/latest?zone=DE"
headers = {
  "auth-token": ""
}

response = requests.get(url, headers=headers)
#print(response.text)
if response.status_code == 200: #überprüft ob Anfrage erfolgreich war
  response_data = response.json()
  power_production_total = response_data['powerProductionTotal']
  power_consumption_total = response_data['powerConsumptionTotal']
else:
  print(f"Error: {response.status_code}")

print(power_production_total)
print(power_consumption_total)