# Python requests Package: 
    # Accessing APIs and web pages
    # Sending data to servers (e.g., login info, form data)
    # Downloading files or JSON content

# Converting JSON to a Python Object: json.loads()
# Converting a Python Object to JSON: json.dumps()

import json
import requests

response = requests.get("https://catfact.ninja/fact")

print(response)  # Should be <Response [200]>

# Convert response to Python dict
data = response.json() 
print(type(data))  # <class 'dict'>

data_json = json.dumps(data)
print(type(data_json))
# output should be str(JSON string): It's a string representation of JSON — like what you’d send over a network or save in a .json file.

print(data['fact'])
