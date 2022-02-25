from backend.api_query.get_data import query_data
import backend

print(backend.__doc__)

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
print(query_data(q))