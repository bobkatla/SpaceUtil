import tests.get_data as source


if __name__ == '__main__':
    query = '''{
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
    resp = source.query_data(query)
    print(resp.text)

