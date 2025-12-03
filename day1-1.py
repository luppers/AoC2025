def main():
    file_path = 'E:\\Repos\\AoC2025\\day1_input.txt'

    dial = 50
    print('the dial starts pointing at ' + str(dial))
    answer = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:

                if line[0] == 'R':
                    dial += int(line[1:])
                elif line[0] == 'L':
                    dial -= int(line[1:])

                if dial > 99 or dial < 0:
                    dial = dial % 100

                print('the dial is rotated ' + line.strip() + ' to point at ' + str(dial))

                if dial == 0:
                    answer += 1

                print('------------')

            print('ANSWER: ' + str(answer))
                    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

if __name__ == "__main__":
    main()

