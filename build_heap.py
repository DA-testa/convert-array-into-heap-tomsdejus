# python3


import fileinput
import glob
import os
import sys


def build_heap(data):
    swaps = []

    for i in range(len(data) // 2 - 1, -1, -1):
        node = i
        
        while True:
            next_node = node * 2 + 1
            if next_node >= len(data):
                break
            if next_node + 1 < len(data) and data[next_node + 1] < data[next_node]:
                next_node += 1
            if data[node] < data[next_node]:
                break

            swaps.append((node, next_node))
            data[next_node], data[node] = data[node], data[next_node]
            node = next_node

    return swaps




def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    input_type = input()
    data =[]
    if input_type == 'F\r':
        file = input()
        location = './tests/'
        path = os.path.join(location, file)
        with open(path) as f:
            data = list(map(int, f.readline().split()))
            n= len(data)
            print(data[0])
            print(n)

        for line in fileinput.input():
            print(line)
            

    elif input_type == 'I\r':
        while True:
            n = int(input())
            if 1 <= n and n <= 100000:
                break;
        data = list(map(int, input().split()))
    #1 ≤ 𝑛 ≤ 100 000; 0 ≤ 𝑖, 𝑗 ≤ 𝑛 − 1; 0 ≤ 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 ≤ 109. All 𝑎𝑖 are distinct.
    # input from keyboard
    


    # checks if lenght of data is the same as the said lenght

    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    if len(swaps) == 0:
        print(0)
    else:
        print(len(swaps))
        for i, j in swaps:
            print(i, j)


if __name__ == "__main__":
    main()
