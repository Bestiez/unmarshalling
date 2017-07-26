import xml.etree.ElementTree as marshall
import csv

class xml_converter():

    @staticmethod
    def header_rows():
        header = []
        tree = marshall.parse('test.xml')
        root = tree.getroot()
        for child in root.findall('country'):
            name = child.get('name')
            header.append(name)
        with open('test.csv', 'a', newline='') as csvfile:
            wtr = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
            wtr.writerow(header)

    @staticmethod
    def inner_rows():
      tree = marshall.parse('test.xml')
      root = tree.getroot()

      for child in root.findall('country'):
          # readinng the column values
          rank = child.find('rank').text
          year = child.find('year').text
          gdppc = child.find('gdppc').text
          name = child.get('name')
          print (rank, name)
          with open('test.csv', 'a', newline='') as csvfile:
             wtr = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
             # add column varibles that should be written to the csv file
             wtr.writerow([rank,year,gdppc])

if __name__ == '__main__':
    xml_converter.header_rows()
    xml_converter.inner_rows()