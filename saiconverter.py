#!/usr/bin/env python3

import csv
import re




def main():

    # Open CSV File based on user input

    # infile_sai = input('\nInput SAI csv filename (include path): ')
    # infile_co = input('\nInput CO csv filename (include path): ')
    # outfile = input('\nOutput csv filename (include path): ')

    infile_sai = ('/home/linuxg33k/dev/csvparser/data/SAIdata/original/ServingAreas02June2020.csv')
    infile_co = ('/home/linuxg33k/dev/csvparser/data/SAIdata/original/CentralOffice02June2020.csv')
    outfile = ('/home/linuxg33k/dev/csvparser/data/SAIdata/modified/ServingAreas_modified.csv')

    # Open CO File
    with open(infile_co, 'r') as co_file:
        co_reader = csv.DictReader(co_file)
        co_data = []
        for row in co_reader:
            co_data.append(row['Description'])

        # CO Data - data used for creating new SAI names
        print(co_data)
        print(len(co_data))
        # quit()

    # Open SAI File
    with open(infile_sai, 'r') as sai_file:

        # Read CSV File
        sai_reader = csv.DictReader(sai_file)

        # Setup Write File

        with open(outfile, 'w', newline='') as sai_outfile:

            # Add same header names
            sai_fieldnames = sai_reader.fieldnames
            writer = csv.DictWriter(sai_outfile, fieldnames=sai_fieldnames)
            writer.writeheader()

            # Parse through data in file
            for row in sai_reader:
                if row['SAName'] != '':
                    print(('Original SAName: {0}').format(row['SAName']))
                    for item in co_data:
                        result = re.findall(r'(\w{4}-' + row['SAName'] +')', item)
                        result_co = re.findall(row['SAName'] + '-CO', item)
                        if result != []:
                            print(item)
                            row['SAName'] = item
                            break
                        if result_co != []:
                            print((item + 'and value is: {0}-{0}').format(row['SAName']))
                            row['SAName'] = row['SAName'] + '-' + row['SAName']
                            break

                # Write the row to a new file   

                writer.writerow(row)

if __name__ == '__main__':
    main()