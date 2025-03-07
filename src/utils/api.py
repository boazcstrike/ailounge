import requests
import json


def generate_chat_response(model, prompt, context=[]):
  url = "http://localhost:11434/api/generate"
  headers = {"Content-Type": "application/json"}
  data = {
      "model": model,
      "prompt": prompt,
      "stream": False,
  }
  if len(context) > 0:
      data.update({"context": context})

  try:
      response = requests.post(url, headers=headers, data=json.dumps(data))
      response.raise_for_status()
      return response.json()
  except requests.exceptions.RequestException as e:
      print(f"An error occurred: {e}")
      return None