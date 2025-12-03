import math


def main():
    file_path = 'E:\\Repos\\AoC2025\\day1_input.txt'

    dial = 50
    print('the dial starts pointing at ' + str(dial))
    magnitude = 0
    total = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:

                distance = int(line[1:])

                if line[0] == 'R':
                    magnitude = distance
                elif line[0] == 'L':
                    magnitude = distance * -1

                if magnitude > 0:
                    while magnitude != 0:
                        dial += 1
                        magnitude -= 1
                        if (dial == 0 or dial % 100 == 0):
                            total += 1
                else:
                    while magnitude != 0:
                        dial -= 1
                        magnitude += 1
                        if (dial == 0 or dial % 100 == 0):
                            total += 1

            print('ANSWER: ' + str(total))                
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

if __name__ == "__main__":
    main()

