# "simple-chatgpt-api" setup
import requests

api_url = "https://simple-chatgpt-api.p.rapidapi.com/ask"
api_headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "e2af93470amsh08465450b0656c3p178d87jsndbaae8795483",
    "X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
}


# Function to get a response from the "simple-chatgpt-api"
def get_answer(question):
  payload = {"question": question}
  response = requests.post(api_url, json=payload, headers=api_headers)
  data = response.json()
  return data.get('answer')
