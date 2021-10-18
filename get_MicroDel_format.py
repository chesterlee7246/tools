# -*- coding: UTF-8 -*-
import re
import sys

#usage: python *py 'chr22 17920001 23280000' del
if len(sys.argv) != 3:
    print('Usage: python {} "chr start end" type'.format(sys.argv[0].split('/')[-1]))
else:
    coordinate = sys.argv[1] #chr1 10000 20000
    variation = sys.argv[2] #del/dup
    cytoband = '/home/lixinxu806/python_script/cytoBand_hg19.txt'
    [chr,start,end] = coordinate.strip().split()
    #print(chr,start,end)
    #cytoband_dict = {}
    bandstart = bandend = ''
    f=open(cytoband,'r')
    for line in f:
        line=line.strip().split()
        #print(line)
        if line[0] == chr:
            #print(chr)
            if int(line[1]) < int(start) < int(line[2]):
                bandstart = line[3]
            if int(line[1]) < int(end) < int(line[2]):
                bandend = line[3]
            if bandstart != '' and bandend != '':
                break
        else:
            pass
    f.close()

    if bandstart and bandend:
        if variation == 'dup':
            chrnumber = re.findall('(?<=chr).*',chr)[0]
            length = str(round( (int(end)-int(start))/1000000,2 ))+'Mb'
            print('dup('+chrnumber+')'+'('+bandstart+'-'+bandend+')'+'seq[GRCh37/hg19]'+'('+start+'-'+end+')'+'x3 '+'【'+length+'】')
        elif variation == 'del':
            chrnumber = re.findall('(?<=chr).*',chr)[0]
            length = str(round((int(end)-int(start))/1000000,2))+'Mb'
            print('del('+chrnumber+')'+'('+bandstart+'-'+bandend+')'+'seq[GRCh37/hg19]'+'('+start+'-'+end+')'+'x1'+'【'+length+'】')
    else:
        print('bandstart or bandend not found.')
