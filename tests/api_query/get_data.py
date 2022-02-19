import requests
from requests.structures import CaseInsensitiveDict

from tests.api_query.parameters_connect import url_auth, url_query, api_key, api_secret


# make the request to get the token
def get_token_raw(url, key, secret):
    # header set up
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    req = {"ApiKey": key, "ApiSecret": secret}

    return requests.post(url, headers=headers, json=req)

def get_data_raw(url, token, query):
    # header set up
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    return requests.post(url, headers=headers, json={"query": query})

def query_full_data(query):
    raw_token = get_token_raw(url_auth, api_key, api_secret)
    token = raw_token.json()['idToken']
    if int(raw_token.json()['expiresIn']) < 100:
        # token is about to expire warning
        print("The token will expire soon, please check!")

    raw_data = get_data_raw(url_query, token, query)
    return raw_data.json()

def query_data(query):
    data_full = query_full_data(query)

    err = data_full["errors"]
    data = data_full["data"]

    return ["ERROR", err] if err else data

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
    q2 = '''{
        sensorInstallations() {
            sensor sensorId
        }
    }'''

    q_err = "{floorSpaces {ho he}}"
    data = query_data(q)
    print(data)
