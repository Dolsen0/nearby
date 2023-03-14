import requests
import json

# Load the API key from the JSON file
with open('apiKey.json') as api_key_json:
    api_key = json.load(api_key_json)['api_key']

# Set the API endpoint and parameters
api_endpoint = 'https://api.yelp.com/v3/businesses/search'
params = {
    'location': '33065',
    'term': 'Italian',
    'limit': 10,
    'sort_by': 'rating'
}

# Set the headers with the API key
headers = {
    'Authorization': f'Bearer {api_key}'
}

# Make the request to the API
response = requests.get(api_endpoint, headers=headers, params=params)

# Convert the response to a JSON object
businesses = json.loads(response.text)

# Print the names of the businesses
for i, business in enumerate(businesses['businesses']):
    print(f"{i+1}: {business['name']} \nRating: {business['rating']} stars \nYelp Link:\n{business['url']} \n")
