import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access API key and endpoint from environment variables
api_key = os.getenv('API_KEY')
endpoint = os.getenv('ENDPOINT')

# Define headers and data
headers = {
    'Content-Type': 'application/json',
    'api-key': api_key
}

# Define the prompt and other parameters for the API request
data = {
    "prompt": "Hello world,",     # Ensure your prompt is a string
    "max_tokens": 300,                  # Ensure max_tokens is an integer
    "temperature": 0.7                 # Optional, but it's a valid parameter
}

# Make the API request
response = requests.post(endpoint, headers=headers, json=data)

# Print the response
if response.status_code == 200:
    result = response.json()
    print(result['choices'][0]['text'])
else:
    print(f"Error: {response.status_code}, {response.text}")
