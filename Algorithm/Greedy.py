# _*_ coding:utf8 _*_

states_needed = set (["mt","wa","or","id","nv","ut","ca","az"]) #传入一个数组，转换为集合

stations = {}
stations["kone"] = set(["id","nv","ut"])
stations["ktwo"] = set(["wa","id","mt"])
stations["kthree"] = set (["or","nv","ca"])
stations["kfour"] = set (["nv","ut"])
stations["kfive"] = set (["ca","az"])
final_stations = set()


while states_needed:
    best_stations = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -=states_covered
    final_stations.add(best_station)
print(final_stations)






fruits = set (["avocado","tomato","banana"])
vegetables = set (["beets","carrots","tomato"])
# fruits | vegetables ————————并集0......
# fruits & vegetables ————————交集
# fruits - vegetables ————————差