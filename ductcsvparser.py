#!/usr/bin/env python3

import csv
import re




def main():

    # Open CSV File based on user input

    infile = input('\nInput csv filename (include path): ')
    outfile = input('\nOutput csv filename (include path): ')

    # infile = ('/home/bcalvert/dev/csvparser/data/M4DuctReport.csv')
    # outfile = ('/home/bcalvert/dev/csvparser/data/M4DuctReportScrubbed.csv')

    # Open csvfile
    with open(infile, 'r') as csvfile:

        # Read CSV File
        reader = csv.DictReader(csvfile)

        # Setup Write File

        with open(outfile, 'w', newline='') as csvoutfile:

            # Add same header names
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(csvoutfile, fieldnames=fieldnames)
            writer.writeheader()

            # Parse through data in file
            for row in reader:
                if row['NumDucts'] != '':
                    print(('Original NumDucts: {0}').format(row['NumDucts']))
                    data = re.findall('(\d{1,1}\.\d{1,2})', row['NumDucts'])
                    data_no_x = re.findall('X(\.\d{1,2})', row['NumDucts'])
                    if data != []:
                        row['Size'] = data[0]
                        # row['NumDucts'] = '1X' + row['NumDucts'].strip('X' + row['Size'] + 'W|H')
                        ducts = re.findall('(\d{1}X\d{1})X', row['NumDucts'])
                        ducts_no_x = re.findall('(\d{1})X', row['NumDucts'])
                        if ducts != []:
                            row['NumDucts'] = ducts[0]
                        elif ducts_no_x != []:
                            row['NumDucts'] = '1X' + ducts_no_x[0]
                        else:
                            pass
                        if len(row['NumDucts']) < 3:
                            row['NumDucts'] = row['NumDucts'] + '1'
                        print(('Size: {0}, New NumDucts: {1}').format(row['Size'], row['NumDucts']))
                    if data_no_x != []:
                        row['Size'] = data_no_x[0]
                        row['NumDucts'] = '1X1'
                        print(('Size: {0}, New NumDucts: {1}').format(row['Size'], row['NumDucts']))
                    print('-'*8)
                
                # Write the row to a new file    

                writer.writerow(row)

if __name__ == '__main__':
    main()