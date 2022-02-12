import requests
from requests.structures import CaseInsensitiveDict

from parameters_connect import url_auth, url_query, api_key, api_secret


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

def query_full_data(query):
    raw_token = get_token_raw(url_auth, api_key, api_secret)
    token = raw_token.json()['idToken']
    raw_data = get_data_raw(url_query, token, query)
    data = raw_data.json()

    return data

def query_data(query):
    data_full = query_full_data(query)
    err = data_full["errors"]
    data = data_full["data"]
    if err:
        return ["ERROR", err]
    else:
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
    q2 = '''{
        sensorInstallations() {
            sensor sensorId
        }
    }'''

    q_err = "{floorSpaces {ho he}}"
    data = query_data(q_err)
    print(data)
