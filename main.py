import requests
from datetime import datetime
import os


api_id = os.environ["API_ID"]
apikey = os.environ["API_KEY"]
sheet_id = os.environ["SHEET_ID"]
sheet_pw = os.environ["SHEET_PW"]
base_url = "https://trackapi.nutritionix.com"
worksheet_url = "https://api.sheety.co/181bf5157ef7a9c1341ce2685d721a2c/workoutTracking/workouts"

exercise_url = "/v2/natural/exercise"
query = input("Tell me which exercise you did: ")
headers = {
    "x-app-id": api_id,
    "x-app-key": apikey,
    "x-remote-user-id": "0"
}

params = {
    "query": query,
    "gender": "male",
    "weight_kg": os.environ["WEIGHT_KG"],
    "height_cm": os.environ["HEIGHT_CM"],
    "age": 26
}

response = requests.post(url=f"{base_url}{exercise_url}", json=params, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


sheety_params = {
    "email": {
        "name": "2모나",
        "email": os.environ["EMAIL"]
    }
}

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=worksheet_url, json=sheet_input, auth=(sheet_id, sheet_pw))
print(sheet_response.text)