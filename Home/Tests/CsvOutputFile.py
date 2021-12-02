# coding=utf-8


import csv
import os
from datetime import datetime

class CsvOutput() :
    FileName = ""
    workbook = None
    worksheet = None
    RowIndex = 0

    def __init__(self,
                 fileName,
                 handers,
                 data
                ):

        self.className = self.__class__.__name__
        self.RowIndex = 0

        self.filePath = fileName

        self.FilesFolder = os.getcwd()
        if not ('Home' in self.FilesFolder):
            self.FilesFolder = os.path.abspath(os.getcwd() + os.path.sep + 'Home' + os.path.sep + 'ResultsFiles')
        else:
            ''' case when the run is launched from Home/Tests '''
            self.FilesFolder = os.path.abspath(os.getcwd() + os.path.sep + '..' + os.path.sep + 'ResultsFiles')

        print self.className + ': file folder= {0}'.format(self.FilesFolder)
        self.filePath = os.path.abspath(self.FilesFolder + os.path.sep + self.filePath)
        print self.className + ': file path= {0}'.format(self.filePath)

        self.filePath = self.filePath + '-{0}.csv'.format(datetime.now().strftime("%d-%b-%Y-%Hh%Mm%S"))
        print self.className + ': file path= {0}'.format(self.filePath)
        self.has_write(handers, data)


    def has_write(self, handers, data):
        with open(self.filePath, "wb", ) as datacsv:
            self.csvwriter = csv.writer(datacsv, dialect=("excel"))
            self.csvwriter.writerow(handers)
            for rowArr in data:
                self.csvwriter.writerow(rowArr)

if __name__ == '__main__':
    handers = (['a', 'b', 'c', 'd', 'e', 'f'])
    data = [[1,2,3,4,5,6],
            [2,3,4,5,6,7]]
    csvOutput = CsvOutput('test', handers, data)
