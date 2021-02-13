import csv

def filter_duplicates():
    for bot_num in range(1,33):
        bot_csv = "data/usernames{}.csv".format(bot_num)
        bot_dict = {}
        with open(bot_csv, 'r', encoding='utf-8', newline='') as unfiltered:
            reader = csv.reader(unfiltered, delimiter = ',', quotechar='"')
            for row in reader:
                if row[0] not in bot_dict:
                    bot_dict[row[0]] = []
                else:
                    if row[1] not in bot_dict[row[0]]:
                        bot_dict[row[0]].append(row[1])
        filtered_file = "data/filtered{}.csv".format(bot_num)
        unfiltered.close()

        with open(filtered_file, 'w', newline='') as filtered:
            writer = csv.writer(filtered, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for key in bot_dict:
                for following in bot_dict[key]:
                    writer.writerow([key, following])
        filtered.close()

def main():
    print("filtering duplicates...")
    filter_duplicates()

if __name__ == '__main__':
    main()
