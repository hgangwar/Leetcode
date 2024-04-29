#!/bin/python3

import math
import os
import random
import re
import sys

def shortestReach(n, edges, s):
    from collections import defaultdict
    import heapq as hq
    graph=defaultdict(list)
    min_weight=defaultdict(lambda: float('inf'))
    for x in edges:
        src, end, weight=x
        if (min_weight[(src, end)]>weight and min_weight[(end,src)]>weight):
            graph[src]+=[(end, weight)]
            graph[end]+=[(src, weight)]
            min_weight[(src,end)]=weight
            min_weight[(end,src)]=weight
    dist=[float('inf') for x in range(n) ]
    dist[s-1]=0
    heap=[(0, s)]
    hq.heapify(heap)
    while(heap):
        weight, node=hq.heappop(heap)
        for child, c_weight in graph[node]:
            new_weight=weight+c_weight
            if(new_weight < dist[child-1]):
                dist[child-1]=new_weight
                hq.heappush(heap, (new_weight, child))
    result=[]
    for i in range(len(dist)):
        if dist[i]==float('inf'):
            result.append(-1)
        elif (i!=s-1):
            result.append(dist[i])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
