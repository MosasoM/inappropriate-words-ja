import sys
import os
import argparse

def add_and_sort_word(args):
    target_file_path = os.path.join(os.path.dirname(__file__), args.filename)
    word_list = set()

    with open(target_file_path,"r",encoding="utf-8") as f:
        words = f.read().split("\n")
        for w in words:
            if len(w)>0:
                word_list.add(w)

    if args.words:
        for w in args.words:
            word_list.add(w)
    else:
        with open(os.path.join(os.path.dirname(__file__), args.source),encoding="utf-8") as f:
            words = f.read().split("\n")
            for w in words:
                if len(w)>0:
                    word_list.add(w)

    word_list = list(word_list)
    word_list.sort()
    with open(target_file_path,"w",encoding="utf-8") as f:
        for w in word_list:
            f.write(f"{w}\n")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='filename added words eg.Sexual.txt')
    parser.add_argument('-w','--words', help='words to add',nargs='*')
    parser.add_argument('-s', '--source',help='file which lists words to add')
    args = parser.parse_args()

    add_and_sort_word(args)
