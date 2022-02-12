# To hold parameters/ constants
import os

# Note that they are HTTPS, maybe need SSL cert, ofcourse can do verify=False
url_auth = "https://core-api.app.xysense.io/api/v1/auth"
url_query = "https://core-api.app.xysense.io/api/v1/query"

# we need this from XY Sense, normally this should be in the env not here
api_key = "bob-tests-monash-uni-api-key"
api_secret = str(os.getenv('SPACE_SECRET'))