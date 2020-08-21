import sys
import os
import argparse
import re

def make_masked(args):
    bopo_dic = {}
    with open(os.path.join(os.path.dirname(__file__), "bopomofo_map.txt")) as f:
        temp = f.read().split("\n")
        for line in temp:
            hoge = line.split(",")
            bopo_dic[hoge[0]] = hoge[1:]

    source_file_path = os.path.join(os.path.dirname(__file__), args.filename)
    word_list = set()

    with open(source_file_path,"r",encoding="utf-8") as f:
        words = f.read().split("\n")
        for w in words:
            if len(w)>0:
                word_list.add(w)

    bopo_list = set()
    for w in word_list:
        buf = set()
        buf.add(w)
        flag = False
        for key in bopo_dic.keys():
            temp = buf.copy()
            for bopo in bopo_dic[key]:
                for word in buf:
                    if key in word:
                        subed = re.sub(key,bopo,word)
                        temp.add(subed)
                        flag = True
            buf = temp.copy()

        if flag:
            for val in buf:
                bopo_list.add(val)

    bopo_list = list(bopo_list)
    bopo_list.sort()
    
    new_filename = args.filename.split(".")[0]+"_with_bopo."+args.filename.split(".")[1]
    with open(os.path.join(os.path.dirname(__file__), new_filename),"w") as f:
        for w in bopo_list:
            f.write(f"{w}\n")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='filename added words eg.Sexual.txt')
    args = parser.parse_args()
    make_masked(args)