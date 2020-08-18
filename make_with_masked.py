import sys
import os
import argparse

def make_masked(args):
    source_file_path = os.path.join(os.path.dirname(__file__), args.filename)
    word_list = set()

    with open(source_file_path,"r",encoding="utf-8") as f:
        words = f.read().split("\n")
        for w in words:
            if len(w)>0:
                word_list.add(w)

    mask_tokens = ["○","◯","⚪","O","o","✗","x","X","□","■"]

    masked_list = set()

    for w in word_list:
        char_list = list(w)
        for mask in mask_tokens:
            for i in range(len(w)//2):
                char_list[i*2+1] = mask
            masked_list.add("".join(char_list))
    
    masked_list = list(masked_list)
    masked_list.sort()
    new_filename = args.filename.split(".")[0]+"_with_mask."+args.filename.split(".")[1]
    with open(os.path.join(os.path.dirname(__file__), new_filename),"w") as f:
        for w in masked_list:
            f.write(f"{w}\n")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='filename added words eg.Sexual.txt')
    args = parser.parse_args()
    make_masked(args)