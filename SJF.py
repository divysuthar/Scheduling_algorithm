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

    for i in range(process):
        print("Enter arrival time ", end='')
        arrival.append(int(input()))
        print("Enter burst time ", end='')
        burst.append(int(input()))

    completed = 0

    p = [] # priority queue Burst completed arrival number

    v = [] # Answer

    time = 0
    while True:
        for i in range(process):
            if arrival[i] <= time and procompleted[i] == 0:
                heapq.heappush(p, [burst[i], arrival[i], i])
                # print(i)
                procompleted[i] = 1
        if len(p):
            running_process = heapq.heappop(p)
            total = running_process[0] + time
            while time < total:
                temp = []
                for i in range(process):
                    if i == running_process[2]:
                        temp.append(1)
                    else:
                        temp.append(0)
                v.append(temp)
                if arrival[i] <= time and procompleted[i] == 0:
                    heapq.heappush(p, [burst[i], arrival[i], i])
                    procompleted[i] = 1
                time += 1
            completed += 1
            if completed == process:
                break
            time -= 1
        else:
            temp = []
            for i in range(process):
                # print(i)
                temp.append(0)
            v.append(temp)
        time += 1
    
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
    plt.title('SJF')
    plt.show()

if __name__ == "__main__":
    n = 1
    while n > 0:
        solve()
        n -= 1