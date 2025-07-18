def get_changing_words(file):
    """Extract words the need changing from a file."""
    ch_words=[]
    with open(file,"r") as test:
        text = test.read()
        words = text.split()
        for word in words:
            if word.isupper() and len(word) > 3 :
                ch_words.append(word)
    return ch_words

def user_input(words):
    """Takes user input for new words."""
    new_words=[]
    for word in words:
        new_words.append(input(f"Enter an {word.lower()}: \n"))
    return new_words

def replace_words(oldfile,newfile):
    """Replaces the old words with new words and creates a new file."""
    with open(oldfile, "r") as O:
        with open(newfile,"w") as W:
            oldwords=get_changing_words(oldfile)
            newwords=user_input(oldwords)
            text = O.read()
            for i, word in enumerate(oldwords):
                if word in text:
                    text= text.replace(word,newwords[i])
            W.write(text)
            print(text)

if __name__ == "__main__":
    old_file= input("please enter the name of the file you want to open:\n")
    new_file= input("Please enter the name of the file you want to create:\n")

    replace_words(old_file,new_file)