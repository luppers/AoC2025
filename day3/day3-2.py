def main():
    file_path = './day3/day3-input.txt'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            total = 0
            
            for line in file:
                line = line.strip()
                curr = -1
                maximum = 0
                arr = ["0" for _ in range(12)]
                for i in range(12):
                    for j in range(curr + 1, 
                                   len(line) - 12 + i + 1):
                        if line[j] > arr[i]:
                            arr[i] = line[j]
                            curr = j

                maximum = int(''.join(arr))

                print(maximum)
                total += maximum
            print('------------')
            print(total)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

if __name__ == "__main__":
    main()