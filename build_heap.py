# python3


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

            swaps.append((next_node, node))
            data[next_node], data[node] = data[node], data[next_node]
            node = next_node
    
    return swaps




def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    #1 ≤ 𝑛 ≤ 100 000; 0 ≤ 𝑖, 𝑗 ≤ 𝑛 − 1; 0 ≤ 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 ≤ 109. All 𝑎𝑖 are distinct.
    # input from keyboard
    
    while True:
        n = int(input())
        if 1 <= n and n <= 100000:
            break;
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght

    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)
    print(swaps)
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
