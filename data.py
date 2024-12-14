import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

#18 is computer science questions
#17 is a physics questions
# 19 is maths questions
# 10 is literature


