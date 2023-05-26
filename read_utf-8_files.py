#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ofer
#
# Created:     02/07/2015
# Copyright:   (c) Ofer 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import io
import sys
f = io.open('course_list.txt', mode="r", encoding="utf-8")
line = f.next()

l = line.split()

for i in l:
    sys.stdout.write(i + " ")



##
##
##orig_res_path = "Y:\\Documents\\Braude\\2015\\DSAL\\Projects\\Project2_2H15\\"
##file_names = ["cir1","cir2","cir3","cir4"]
##
##
##for name in file_names:
##    f = open(orig_res_path+name+".out")
##    f_stud = open(name+".res")
##
##    for line in f:
##        st_line = f_stud.next()
##        if st_line != line:
##            print name,": ",line,"vs",st_line
##


def main():
    pass

if __name__ == '__main__':
    main()
