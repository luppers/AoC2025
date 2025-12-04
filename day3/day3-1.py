def main():
    file_path = './day3/day3-input.txt'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            total = 0
            
            for line in file:
                line = line.strip()
                x = 0
                i = 0
                maximum = 0
                for char in line:
                    i += 1
                    x = int(char)*10
                    for char2 in line[i:]:
                        n = x + int(char2)
                        if n > maximum:
                            maximum = n
                print(maximum)
                total += maximum
            print('------------')
            print(total)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

if __name__ == "__main__":
    main()