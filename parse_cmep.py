#!/bin/python3

'''
note: this uses Python 3
 
This will parse a delimited CMEP file into single row CSV records. 

Usage				: python3 parse_cmep.py -f CMEP_Format_sample.txt -d '\t' -r 14 --header

Outputted rows 		: [Meter ID], [Constant Calculation], [Timestamp], [Quality Code], [Value]
Outputted filename	: parsed_cmep_[commodity id]_[unit of measurement]_[process id].csv

Author 				: Mike Czabator

example				: 

mike@lenovo ~/mike/tools/cmep_file_parser
$ python3 parse_cmep.py --delimiter '\t' --file CMEP_Format_sample.txt --header
***************
Input file           : CMEP_Format_sample.txt
input CMEP file lines: 10000
output CSV lines     : 96755
time                 : 2.2290380001068115 seconds / 0 minutes
***************

mike@lenovo ~/mike/tools/cmep_file_parser
$ head parsed_cmep_E_KWH.27772.csv
123456,1,201811020700,,1.23
123456,1,201811020800,,1.173
123456,1,201811020900,,1.173
123456,1,201811021000,,1.173
123456,1,201811021100,,1.173
123456,1,201811021200,,1.23
123456,1,201811021300,,1.23
123456,1,201811021400,,1.288
123456,1,201811021500,,1.23
123456,1,201811021600,,1.23

'''
import argparse
import os
import codecs
import time

def unescaped_str(arg_str):
	return codecs.decode(str(arg_str), 'unicode_escape')
	
#get arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",default='CMEP_Format_sample.txt',type=str,help="filename of CMEP file (ex: /tmp/CMEP_Format_sample.txt)",required=False)
parser.add_argument("-d","--delimiter",default='\t',type=unescaped_str,help="Delimiter used in CMEP file, in quotes ( ex: ',' , '|', '\\t' )",required=False)
parser.add_argument("-r","--read_start_column",default=14,type=int,help="Column which interval reads start in CMEP file (default: 14)",required=False)
parser.add_argument('--header', dest='skip_header', action='store_true',help="File contains a header (default)")
parser.add_argument('--no-header', dest='skip_header', action='store_false',help="File does NOT contain a header")
parser.set_defaults(skip_header=True)
args = parser.parse_args()


def parse_file(): 
	startTime = time.time()
	line_number = 0
	record_count= 0
	with open(args.file,"r") as f:
		for line in f:
			read_start_column = args.read_start_column
			
			#skip header line if --no-header is used
			if (line_number == 0 and args.skip_header == True):
				line_number+=1
				continue
				
			#skip blank lines
			if(line in ('\n','\r\n')):
				continue
			
			line_number+=1
			record = []
			record = line.split(args.delimiter) #split by the delimiter 

			#open file  parsed_cmep_+"+[commodity id]+"_"+[units]+"."+[process id].csv
			outfile = open("parsed_cmep_"+record[9]+"_"+record[10]+"."+str(os.getpid())+".csv","a")
			while read_start_column <= len(record):
				if record[read_start_column] == "": 
					read_start_column+=3
					continue

				try: # METER ID, Constant Calculation, Timestamp, Quality code, Value
					outline = '{0},{1},{2},{3},{4}\n'.format(record[7],record[11],record[read_start_column],record[read_start_column+1],record[read_start_column+2])
					record_count+=1
					outfile.write(outline)
				except:
					break
				read_start_column+=3
		f.close()
		outfile.close()
		endTime = time.time()
		print("\n***************\nInput file           : "+args.file+"\ninput CMEP file lines: "+str(line_number)+"\noutput CSV lines     : "+str(record_count)+"\ntime                 : "+str(endTime-startTime)+" seconds / "+str(((endTime-startTime)/60))+" minutes \n***************\n")
		
if __name__== "__main__":
  parse_file()
