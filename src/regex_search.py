from pathlib import Path
import sys
def prompt_input():
    """Prompts input from the user in a loop only breaks when valid path is given"""
    while True:
        path = Path(input("Please enter files location, leave empty if you want currect dir:\n").strip())
        if path.exists() and path.is_dir():
            return path
        else:
            print("Invalid path try again") 

def get_file_names(dir_path = None) -> list[str]:
    """Gets local .txt file names"""
    directory = dir_path or Path.cwd()
    files =list(directory.glob('*.txt'))
    filenames=[]
    for file in files:
        filenames.append(file.name)
    return(filenames)

def key_string() -> str:
    """Asks user to input a string that will be used to search local files"""
    x=input("Please write a sentence or word you would like to search for in the local txt files:\n")
    return(x)

def search_local_files(string,filenames) -> list[Path]:
    """Searches given file names with given string to find a match"""
    matches=[]
    for file in filenames:
        with open(file,'r') as open_file:
            if string in open_file.read():
                matches.append(open_file)
    return matches

if __name__ == "__main__":
    try:
        directory=  prompt_input()
        matched = search_local_files(key_string(),get_file_names(directory))
        if matched:
            print("Found your text in")
            for f in matched:
                print("*", f.name)
        else:
            print("No matches found!")
    except KeyboardInterrupt:
        sys.exit()