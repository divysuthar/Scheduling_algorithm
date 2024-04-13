import heapq
import matplotlib.pyplot as plt
import numpy as np

def solve():
    print("Enter number of processes ", end='')
    process = int(input())

    arrival = []
    burst = []
    procompleted = [0] * process
    finish = []
    priority = []

    for i in range(process):
        print("Enter arrival time ", end='')
        arrival.append(int(input()))
        print("Enter burst time ", end='')
        burst.append(int(input()))
        print("Enter priority ", end='')
        priority.append(int(input()))

    completed = 0

    p = [] # priority queue priority Burst number

    v = [] * process # Answer

    time = 0
    while True:
        for i in range(process):
            if arrival[i] <= time and procompleted[i] == 0:
                heapq.heappush(p, [priority[i], burst[i], i])
                procompleted[i] = 1
        if len(p):
            runnn = heapq.heappop(p)
            print(runnn)
            # print(runnn[0] , " " , runnn[1] , " " , runnn[2])
            temp = []
            for i in range(process):
                if i == runnn[2]:
                    temp.append(1)
                else:
                    temp.append(0)
            v.append(temp)
            runnn[1] -= 1
            if runnn[1] == 0:
                completed += 1
            else:
                heapq.heappush(p, runnn)
            if completed == process:
                break
        else:
            temp = []
            for i in range(process):
                # print(i)
                temp.append(0)
            v.append(temp)
        time += 1
                 
    # print(v)
    
    for i in range(process):
        last_ind = 0
        for j in range(len(v)):
            print(v[j][i], end='')
            if v[j][i] == 1:
                last_ind = j
        finish.append(last_ind + 1)
        print()
        
    matrix_vec = np.array(v)
    
    nonzero = np.argwhere(matrix_vec == 1)
    
    for i, j in nonzero:
        plt.fill([i, i + 1, i + 1, i], [len(matrix_vec) - j - 1, len(matrix_vec) - j - 1, len(matrix_vec) - j, len(matrix_vec) - j], 'blue')
    
        
    name = 'A'
    avg_wt = 0
    avg_tat = 0
    max_yticks = 0
    for i in range(process):
        print(chr(ord(name) + i), " ", arrival[i], "  ", burst[i], " ", finish[i], "   ", finish[i] - arrival[i], "    ", finish[i] - arrival[i] - burst[i])
        max_yticks = max(max_yticks, finish[i])
        avg_wt += finish[i] - arrival[i] - burst[i]
        avg_tat += finish[i] - arrival[i]

    print("Avg of TAT ", avg_tat / process)
    print("Avg of WT ", avg_wt / process)
    
    plt.xticks(range(max_yticks + 1))
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    n = 1
    # n = int(input())
    while n > 0:
        solve()
        n -= 1
