# Store all the querries for occupancy changes
from get_data import query_data

# Fetching space info 
q_spaceInfo = '''{
    floorSpaces {
        id name
        floor {
            id name 
            location {
                id name
            }
        }
    }
}'''

# Fetching latest Occu
q_latestOccu = '''{
    occupancyChanges {
        nextFrom
        data {
            occupancyStatus headcount floorSpaceId collectedDate
        }
    }
}'''

if __name__ == '__main__':
    data = query_data(q_latestOccu)
    print(data)