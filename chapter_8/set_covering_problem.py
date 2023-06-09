# The states you want to cover
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

# Stations that you’re choosing from
stations = dict()
stations["kone"] = {"id", "nv", "ut"}
stations["ktwo"] = {"wa", "id", "mt"}
stations["kthree"] = {"or", "nv", "ca"}
stations["kfour"] = {"nv", "ut"}
stations["kfive"] = {"ca", "az"}


def my_set_covering(states_needed, stations):
    # To hold the final set of stations you’ll use
    final_stations = set()
    # while states_needed is not None or not empty
    while states_needed:
        # the one that covers the most uncovered states
        best_station = None
        # a set of all the states this station covers that haven’t been covered yet
        states_covered = set()
        for station, states_for_station in stations.items():
            # station_states_covered is a set of states that were in both states_needed and states_for_station.
            # So station_states_covered is the set of uncovered states that this station covers
            # This is a set intersection
            station_states_covered = states_needed & states_for_station
            # You check whether this station covers more states than the current best_station
            if len(station_states_covered) > len(states_covered) and station not in final_stations:
                best_station = station
                states_covered = station_states_covered
        if best_station is not None:
            states_needed -= states_covered
            final_stations.add(best_station)
            stations.pop(best_station)
        else:
            return None
    return final_stations


print(my_set_covering(states_needed, stations))
