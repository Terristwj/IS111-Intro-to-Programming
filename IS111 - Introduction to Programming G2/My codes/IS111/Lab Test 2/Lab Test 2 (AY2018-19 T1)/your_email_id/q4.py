#
# Name: 
# Email ID: 
#

# If needed, you can define your own additional functions here.
# Start of your additional functions.


# End of your additional functions.

def find_stations_within_distance(mrt_map, orig, dist):
    # Modify the code below
    stations = [[orig]]
    while len(stations) < dist+1:
        s = len(stations)-1
        new = []
        for lines in mrt_map:
            for i in range(len(lines)): ## lines[i] is the station in the mrt map
                for stn in stations[s]:
                    if lines[i] == stn:
                        if i == 0:
                            new.append(lines[i+1])
                        elif i == len(lines) - 1:
                            new.append(lines[i-1])
                        else:
                            new.append(lines[i-1])
                            new.append(lines[i+1])
        stations.append(new)
    
    final = []
    for i in range(len(stations)):
        for x in stations[i]:
            if x not in final:
                final.append(x)
    
    final.remove(orig)

    return final
