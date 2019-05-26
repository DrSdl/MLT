"""Count words."""
import re

def count_words(text):
    """Count how many times each unique word occurs in text."""
    counts = dict()  # dictionary of { <word>: <count> } pairs to return
    
    # TODO: Convert to lowercase
    text=text.lower()
    # TODO: Split text into tokens (words), leaving out punctuation
    # (Hint: Use regex to split on non-alphanumeric characters)
    # https://stackoverflow.com/questions/35231285/python-how-to-split-a-string-by-non-alpha-characters
    # https://stackoverflow.com/questions/18936957/count-distinct-words-from-a-pandas-data-frame
    
    #my_text = text.split()
    print(text)
    my_text = re.split('[^a-zA-Z]', text)
    #my_text = my_text.remove('')
    print(my_text)
    # TODO: Aggregate word counts using a dictionary
    
    counts = {} 
    for items in my_text: 
        if len(items)>0:
            counts[items] = my_text.count(items)
    #print(counts)
    return counts


def test_run():
    with open("input.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))
        
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()

