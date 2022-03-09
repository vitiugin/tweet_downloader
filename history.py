import os
import json
import requests

from datetime import datetime

bearer_token='####'

# source — https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Full-Archive-Search/full-archive-search.py

search_url = "https://api.twitter.com/2/tweets/search/all"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': 'twitter',
                'start_time': "2020-03-23T05:40:00Z",
                'end_time': "2020-03-23T05:50:00Z",
                'tweet.fields': 'lang',
                'max_results': 500}


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", search_url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(search_url, headers, query_params)
    with open('out.json', 'w') as outfile: # PATH to directory and name of the file
        outfile.write(str(json.dumps(json_response, indent=4, sort_keys=True)))


if __name__ == "__main__":
    main()
