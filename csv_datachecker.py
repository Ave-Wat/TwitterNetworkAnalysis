import csv

'''A file to check that each bot actually scraped all the accounts
it was supposed to.'''

def get_modi_friends_list():
    modi_friends = []
    with open("modi_friends.csv", "rt", encoding="utf8") as file:
        mycsv = csv.reader(file)
        for row in mycsv:
            modi_friends.append(row[1])
    file.close()
    return modi_friends

def get_friend_list_section(friends_list, list_section_num, divide_list_by = 32):
    '''list_section_num is the section of list you want, from 0 to 1 less than divide_list_by'''

    section_len = len(friends_list)/divide_list_by
    slice_int_1 = int(section_len * list_section_num)
    slice_int_2 = int(section_len * (list_section_num + 1))
    return friends_list[slice_int_1:slice_int_2]

def check_bot_completions():
    modi_friends = get_modi_friends_list()
    for bot_num in range(33):
        complete = ""
        bot_csv = "data/usernames{}.csv".format(bot_num)
        bot_scraping_list = get_friend_list_section(modi_friends, bot_num-1)
        with open(bot_csv, 'r', encoding='utf-8') as bot_completed:
            last_acc_scraped = bot_completed.readlines()[-1].split(',')[0]
            if bot_scraping_list[-1] == last_acc_scraped:
                print("Bot {} complete".format(bot_num))
            else:
                for i in range(bot_scraping_list.length, -1, -1):
                    if last_acc_scraped == bot_scraping_list[i]:
                        print("Bot {} incomplete: last index {}".format(bot_num, i))
    return

def main():
    check_bot_completions()

if __name__ == "__main__":
    main()
