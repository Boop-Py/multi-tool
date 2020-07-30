import random
import linecache 

def username_generator():

    # cheapest way I have found to count number of lines in the text file 
    number_lines_nouns = sum(1 for line in open("data/noun_list.txt"))
    number_lines_adjs = sum(1 for line in open("data/adjective_list.txt"))

    # random line number chosen 
    chosen_noun_line = random.randint(1, number_lines_nouns)
    chosen_adj_line = random.randint(1, number_lines_adjs)
    
    # grab the line using the above number and save as variable
    noun = linecache.getline("data/noun_list.txt", chosen_noun_line).rstrip()
    adj = linecache.getline("data/adjective_list.txt", chosen_adj_line).rstrip()

    # plain version
    plain_username = adj + " " + noun

    # camel cased
    camelcase_username = adj.capitalize() + noun.capitalize()

    # with underscore
    underscored_username = adj + "_" + noun

    # with numbers
    numbered_username = camelcase_username + str(random.choice(range(1, 9999)))

    # leetified
    unleet_string = adj + noun
    leet_replacements = {
                        "a": "4", 
                        "b": "8", 
                        "e": "3", 
                        "g": "6", 
                        "i": "1", 
                        "o": "0", 
                        "s": "5", 
                        "z": "2"
                        }
           
    leet_username = unleet_string.translate(str.maketrans(leet_replacements))
    
    return [plain_username, camelcase_username, underscored_username, numbered_username, leet_username]