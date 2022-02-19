from tests.api_query.get_data import query_data


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