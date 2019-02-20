# parse_cmep.py
Parse a delimited CMEP (California Metering Exchange Protocol) file to a single value row CSV

```
Usage			: python3 parse_cmep.py -f CMEP_Format_sample.txt -d '\t' -r 14 --header

Outputted rows		: [Meter ID], [Timestamp], [Constant Calculation], [Quality Code], [Value]
Outputted filename	: parsed_cmep_[commodity id]_[unit of measurement]_[process id].csv

Author 			: Mike Czabator

example			: 
```
```bash
mike@lenovo ~/mike/tools/cmep_file_parser
$ python3 parse_cmep.py --delimiter '\t' --file CMEP_Format_sample.txt --header

***************
Input file           : CMEP_Format_sample.txt
input CMEP file lines: 10000
output CSV lines     : 96755
***************

mike@lenovo ~/mike/tools/cmep_file_parser
$ head parsed_cmep_E_KWH.27772.csv
123456,201811020700,1,,1.23
123456,201811020800,1,,1.173
123456,201811020900,1,,1.173
123456,201811021000,1,,1.173
123456,201811021100,1,,1.173
123456,201811021200,1,,1.23
123456,201811021300,1,,1.23
123456,201811021400,1,,1.288
123456,201811021500,1,,1.23
123456,201811021600,1,,1.23
```
