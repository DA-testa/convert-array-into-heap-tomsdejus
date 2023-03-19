# python3


import sys


def build_heap(data):
    swaps = []


    for i in range(int(len(data)/2)):
        node = i
        
        while True:
            next_node = node * 2 + 1

            if next_node >= len(data):
                break
            if next_node + 1 < len(data) and data[next_node + 1] < data[next_node]:
                next_node += 1
            if data[node] < data[next_node]:
                break

            swaps.append((next_node, node))
            data[next_node], data[node] = data[node], data[next_node]
            node = next_node
    
    return swaps




def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    n = -1
    input_type = input()
    if input_type == 'F':
        stream = sys.stdin
        while True:
            data = stream.read(1024)
            if len(data) == 0:
                break #EOF
    elif input_type == 'I':
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
