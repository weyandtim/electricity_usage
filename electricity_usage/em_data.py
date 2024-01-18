import requests
import json

def get_power_breakdown(zone="DE", auth_token=""):
    url = f"https://api-access.electricitymaps.com/free-tier/power-breakdown/latest?zone={zone}"
    headers = {
        "auth-token": auth_token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        power_production_total = response_data['powerProductionTotal']
        power_consumption_total = response_data['powerConsumptionTotal']
        return power_production_total, power_consumption_total
    else:
        print(f"Error: {response.status_code}")
        return None, None
