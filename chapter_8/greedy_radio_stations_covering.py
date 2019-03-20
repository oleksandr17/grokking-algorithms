# Reference - https://github.com/egonSchiele/grokking_algorithms/blob/master/08_greedy_algorithms/python/01_set_covering.py

target_states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()
while len(target_states) > 0:
    # FInd station with best coverage
    best_station = None
    best_station_coverage = set()
    for station, states in stations.items():
        coverage = target_states & states
        if len(coverage) > len(best_station_coverage):
            best_station = station
            best_station_coverage = coverage

    # Keep station and update target states set
    final_stations.add(best_station)
    target_states -= best_station_coverage

print(final_stations)
