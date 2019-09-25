inp_str = "The father of a British toddler who went missing thirty eight years ago in Germany has said he never gave up hope that she might still be alive as police arrested a man over her disappearance Military police announced yesterday that they were questioning a man in connection with the case of Katrice Lee, who vanished from a supermarket on her second birthday near a British military base in Germany in November one thousand eight hundred and one Officers reportedly began searching a terraced house in the Moredon area of Swindon in Wiltshire on Monday and made an arrest at the property the next day"
inp_str = inp_str.split()
print(f'input: {inp_str}')
words = []
this_len = 0
max_len = 0
for every in inp_str:
    this_len = len(every)
    print(f'now: {every}')
    if this_len > max_len:
        words = []
        words.append(every)
        max_len = this_len
    elif this_len == max_len:
        words.append(every)
print(words)
