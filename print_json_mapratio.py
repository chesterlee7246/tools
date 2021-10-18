#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
import json
import glob
import os
#import sys

#print(sys.path[0])脚本目录
#print(os.getcwd())当前工作目录
def print_mapratio(filelist):
    i,j=0,0
    if js:
        for file in filelist:
            i+=1
            f = open(file,'r')
            js_data = json.load(f)
            index = file.split('/')[-1].replace('_BamDuplicates.json','')
            maprate=js_data['total_mapped_reads']/js_data['total_reads']
            j+=maprate
            print(index+'\t'+str(round(maprate,4)))
        print('Average'+'\t'+str(round(j/i,4)))
    else:
        print('NO Bam stat json file in current directory!')

if __name__ == "__main__":
    js = glob.glob(os.getcwd()+'/*BamDuplicates.json')
    print_mapratio(js)