import requests
from requests.structures import CaseInsensitiveDict


# Note that they are HTTPS, maybe need SSL cert, ofcourse can do verify=False
url_auth = 'https://core-api.app.xysense.io/api/v1/auth'
url_query = 'https://core-api.app.xysense.io/api/v1/query'

# we need this from XY Sense, normally this should be in the env not here
api_key = ''
api_secret = ''

# make the request to get the token
def get_token_raw(url, key, secret):
    # maybe have to add header?
    req = {'ApiKey': key, 'ApiSecret': secret}
    res = requests.post(url, data=req)
    return res

def get_data_raw(url, token, query):
    # will check the header again
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Accept-Encoding"] = "gzip"
    headers["Authorization"] = "Bearer {token}"

    res = requests.post(url, headers=headers)
    return res

def query_data(query):
    raw_token = get_token_raw(url_auth, api_key, api_secret)
    token = raw_token['idToken'] # need to check syntax again
    raw_data = get_data_raw(url_query, token, query)
    data = raw_data

    return data

if __name__ == '__main__':
    # Can put the testing here
    print('nothing for now')