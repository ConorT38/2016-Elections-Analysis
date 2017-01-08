from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# These are the terms we will search for regarding trump
slurs = {'asshole': 0,'fraud' : 0, 'racist' : 0,'sexist' : 0,'misogynist' : 0,'drumpf': 0, 'xenophob' : 0,'hate' : 0,'wall' : 0,'molest' : 0,'fuck' : 0,'notmypresident' : 0,'homophob' : 0,'evil' : 0}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        for key in slurs:
            if str(key) in current_word.lower():
                slurs[key] += 1
        current_count += count
    else:
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
print slurs
