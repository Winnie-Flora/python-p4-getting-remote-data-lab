import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        requester = requests.get(self.url)

        return requester.content

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)

if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)

    try:
        json_data = requester.load_json()
        print(json_data)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")