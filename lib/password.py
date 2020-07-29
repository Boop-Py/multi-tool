import secrets
import string
import linecache

def password_generator():

    
    #Secrets.choice for high entropy character selection.

    # mixed character password, 12 characters as is recommended.
    char_list = string.ascii_letters + string.digits
    mixed_char_password = ''.join(secrets.choice(char_list) for i in range(12)) 

    # three word memorable password
    number_lines_nouns = sum(1 for line in open("data/noun_list.txt"))
    number_lines_adjs = sum(1 for line in open("data/adjective_list.txt"))
    number_lines_adverbs = sum(1 for line in open("data/short_adverbs.txt"))

    chosen_noun_line = secrets.choice(range(1, number_lines_nouns))
    chosen_adj_line = secrets.choice(range(1, number_lines_adjs))
    chosen_adverb_line = secrets.choice(range(1, number_lines_adverbs))
    
 
    noun = linecache.getline("data/noun_list.txt", chosen_noun_line).rstrip().capitalize()
    adj = linecache.getline("data/adjective_list.txt", chosen_adj_line).rstrip().capitalize()
    adverb = linecache.getline("data/short_adverbs.txt", chosen_adverb_line).rstrip().capitalize()
    
    three_word_password = noun + adj + adverb


    # two word password with replacements
    chosen_adj_line = secrets.choice(range(1, number_lines_adjs))
    chosen_adverb_line = secrets.choice(range(1, number_lines_adverbs))
    adj = linecache.getline("data/adjective_list.txt", chosen_adj_line).rstrip().capitalize()
    adverb = linecache.getline("data/short_adverbs.txt", chosen_adverb_line).rstrip()
    
    plain_password = adj + adverb + ''.join(secrets.choice(char_list) for i in range(1))
    char_replacements = {
                        "l": "1",
                        "o": "0"
                        }

           
    two_word_and_char_password = plain_password.translate(str.maketrans(char_replacements))

    

    return [mixed_char_password, three_word_password, two_word_and_char_password]
    