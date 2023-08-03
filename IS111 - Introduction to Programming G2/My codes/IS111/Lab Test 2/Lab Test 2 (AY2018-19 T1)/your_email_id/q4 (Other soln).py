def stop_forward(map, stop):
    # return next stop, if none return false
    stop_index = map.index(stop)
    if stop_index != len(map) - 1:
        return map[stop_index + 1]
    return False

def stop_backward(map, stop):
    # return prev stop, if none return false
    stop_index = map.index(stop)
    if stop_index != 0:
        return map[stop_index - 1]
    return False

def find_stations_within_distance(mrt_map, orig, dist):
    # distance counter
    counter = 0
    goal = dist
    return_list = [orig]
    # Loop stops when no new stop added
    for stop in return_list:
        # initializing current length and current stop
        current_len = len(return_list)
        current_stop = stop
        # Loop through map to find current stop
        for map in mrt_map:
            if current_stop in map:
                # checking if there is a stop infront or behind - adding if there is
                if stop_forward(map, current_stop) and stop_forward(map, current_stop) not in return_list:
                    return_list.append(stop_forward(map, current_stop))
                if stop_backward(map, current_stop) and stop_backward(map, current_stop) not in return_list:
                    return_list.append(stop_backward(map, current_stop))
        # updating length
        new_len = len(return_list)
        counter += 1
        if counter == goal:
            break
        # increasing goal when more than 1 stop added in this loop
        if counter < dist:
            difference = max((new_len - current_len)  - 1, 0)
            goal += difference
    return_list.remove(orig)
    return return_list