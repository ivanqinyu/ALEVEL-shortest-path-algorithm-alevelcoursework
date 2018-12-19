#!/usr/bin/python
# -*- coding: UTF-8 -*-

import io


def build_subway(files):

    count=0
    dictlines={}
    sub=[]
    subname=""
    isCircle= False
    for string in files:
        if count%3 == 0:
            """
            due to some lines are circle lines.
            the Subway need to update
            """
            if string[0]=="*":
                subname=string[1:].strip("\n")
                isCircle=True
            else:
                subname=string.strip("\n")
        elif count%3 == 1:
            sub = string.strip("\n").split(",")
            if isCircle==True:
                sub.append(sub[0])
        else:
            dictlines[subname]=sub
            isCircle=False
        count+=1
        
    dictlines[subname]=sub
    
         
                
    stations = set()
    for key in dictlines.keys():
        stations.update(set(dictlines[key]))
    system = {}
    for station in stations:
        next_station = {}
        for key in dictlines:
            if station in dictlines[key]:
                line = dictlines[key]
                idx = line.index(station)
                if idx == 0:
                    next_station[line[1]] = key
                elif idx == len(line)-1:
                    next_station[line[idx-1]]=key
                else:
                    next_station[line[idx-1]] = key
                    next_station[line[idx+1]] = key
        system[station] = next_station
    return system


def path_search(subway,start, goal):
    """Find the shortest path from start state to a state
    with min change times such that is_goal(state) is true."""
    if start == goal:
        return [start]
    explored = set() 
    queue = [ [start, ('', 0)] ]
    while queue:
        path = queue.pop(0)
        s = path[-2]
        linenum, changetimes = path[-1]
        if s == goal:
            return path
        for state, action in subway[s].items():
            if state not in explored:
                linechange = changetimes
                explored.add(state)
                if linenum != action:
                    linechange += 1
                path2 = path[:-1] + [action, state, (action, linechange)]
                queue.append(path2)
                queue.sort(key=lambda path:path[-1][-1])
    return []


def search(cityname,start,goal):
    file=open(cityname+".txt","r")
    subway = build_subway(file)
    file.close()
    return(path_search(subway,start, goal))

print (search("nanjing","苜蓿园","大行宫"))
