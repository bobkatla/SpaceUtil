# Store all the querries for occupancy changes

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

# 