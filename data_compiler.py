import csv

def compile_data():
    compiled_data = "data/data.csv"
    with open(compiled_data, 'w', newline='') as final_file:
        writer = csv.writer(final_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for bot_num in range(1,33):
            bot_data = "data/filtered{}.csv".format(bot_num)
            with open(bot_data, 'r', newline='') as bot_data:
                reader = csv.reader(bot_data, delimiter = ',', quotechar='"')
                for row in reader:
                    writer.writerow(row)
            bot_data.close()
    final_file.close()

def main():
    print("compiling data")
    compile_data()

if __name__ == '__main__':
    main()
