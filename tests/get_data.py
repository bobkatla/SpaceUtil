import requests
from requests.structures import CaseInsensitiveDict


# Note that they are HTTPS, maybe need SSL cert, ofcourse can do verify=False
url_auth = "https://core-api.app.xysense.io/api/v1/auth"
url_query = "https://core-api.app.xysense.io/api/v1/query"

# we need this from XY Sense, normally this should be in the env not here
api_key = "bob-tests-monash-uni-api-key"
api_secret = ""

# make the request to get the token
def get_token_raw(url, key, secret):
    # maybe have to add header?
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    req = {"ApiKey": key, "ApiSecret": secret}
    res = requests.post(url, headers=headers, json=req)
    return res

def get_data_raw(url, token, query):
    # will check the header again
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    res = requests.post(url, headers=headers, json={"query": query})
    return res

def query_data(query):
    raw_token = get_token_raw(url_auth, api_key, api_secret)
    token = raw_token.json()['idToken']
    raw_data = get_data_raw(url_query, token, query)
    data = raw_data.json()["data"]

    return data

if __name__ == '__main__':
    # Can put the testing here
    q = '''{
            floorSpaces {
                id name
                floor {
                    id name
                    location {
                        id name
                    }
                }
            }
        }
    '''
    data = query_data(q)
    print(data)
