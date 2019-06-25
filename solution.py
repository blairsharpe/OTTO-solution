# Author: Blair Sharpe
# Date: 06/21/2019

from collections import defaultdict
import math
from graph import Graph
import pdb
import sys

def time_for_travel(adjacent_node, station):

    """Computes the time to travel from two stations with station work

    Keyword arguments:
    adjacent_node --  the first station
    station -- the second station
    """
    # The time to do work on a station is 10 seconds
    time_to_do_work = 10
    # Find the two points from the station information dictionary (x1, y1) and (x2, y2)
    x1 = station_information[adjacent_node][0]
    y1 = station_information[adjacent_node][1]
    x2 = station_information[station][0]
    y2 = station_information[station][1]
    # If the robot is moving directly from the source to the target, no station work will be done
    if(adjacent_node == stations - 1 and station == 0):
        time_to_do_work = 0
    # time (s) = 1/2 (seconds/meter) * distance (m) + time to complete station (s)
    time = (1/2) * distance([x1, y1], [x2, y2]) + time_to_do_work

    return time

def distance(p0, p1):

    """Computes the distance between two coordinate points

    Keyword arguments:
    p0 --  the first point (x1, y1)
    p1 -- the second point (x2, y2)
    """
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def create_station_graph():

    """ Creates a graph with number of stations with weights in units of time
    """
    g = Graph(stations)
    # When creating the graph, there are three rules:
    #   1. When creating the stations, the next node number is itself plus one
    #   2. The number of possiblities from that station are destination station # - current station #
    #   3. The graph is exhausted when, the next station is the max # of stations
    for station in range(0, stations):
        for adjacent_node in range(station + 1, stations):
            # If they are two consecutive find the time it takes for those two stations
            if(adjacent_node - 1 == station):
                time = time_for_travel(adjacent_node, station)
                g.addEdge(station, adjacent_node, time)
            # If they are not consecutive then add the penalties for the stations in between
            else:
                penalty = 0
                for station_for_penalty in range(station + 1, adjacent_node):
                    penalty = penalty + station_information[station_for_penalty][2]
                time = time_for_travel(adjacent_node, station)
                g.addEdge(station, adjacent_node, penalty + time)

    return g

def find_shortest_path():

    global station_information
    global stations
    with open(sys.stdin.readline().strip('\n'), "r") as f:
        next(f)
        for line in f:
            line_array  = line.split()
            # If we are at a line where array size is one, it is not station information
            if(len(line_array) != 1):
                station_information[stations] = list(map(int, line_array))
                stations = stations + 1
            else:
                # Add the source and target stations
                station_information[0] = [0, 0]
                station_information[stations] = [100, 100]
                stations = stations + 1
                g = create_station_graph()
                # Find the shortest path form node 0 as the source
                g.shortestPath(0)
                # clear the station map
                station_information = {}
                stations = 1

if __name__ == "__main__":

    station_information = {}
    stations = 1

    find_shortest_path()


