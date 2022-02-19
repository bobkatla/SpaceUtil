# just a playground

from get_data import query_data


q_t = '''{
    floors {
        id name
        activeSensors totalSensors
        latestSightingCount
    }
}'''

q_t_2 = '''{
    mutation generateOccupancyEvents {
        generateOccupancyEvents(id: "c0f84754-c5e3-409c-a252-5fc2985b5817", count: 1) {
            floorSpaceId previousOccupancyStatus occupancyStatus
        }
    }
}'''

if __name__ == "__main__":
    data = query_data(q_t)
    print(data)