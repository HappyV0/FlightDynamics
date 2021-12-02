# coding=utf-8

'''
    author: V0
    date: 2021/12/01
'''

from Home.Config.YmlInput import YmlInput

class BadaInfo(object):
    upHeight = 40                           #前进飞行高度
    cruiseMetersSecond = 101                #最大飛行速度m/s
    cruiseHeight = 400                      #巡航飞行高度
    def __init__(self, fileName = 'AircraftConfig.yml'):
        ymlInput = YmlInput(fileName)
        dicData = ymlInput.getDicData()
        if 'upHeight' in dicData:
            self.upHeight = dicData['upHeight']
        if 'cruiseMetersSecond' in dicData:
            self.cruiseMetersSecond = dicData['cruiseMetersSecond']
        if 'cruiseHeight' in dicData:
            self.cruiseHeight = dicData['cruiseHeight']

    def getUpHeight(self):
        return self.upHeight
    def setUpHeight(self, upHeight):
        self.upHeight = upHeight
    def getCruiseMetersSecond(self):
        return self.cruiseMetersSecond
    def setCruiseMetersSecond(self, cruiseMetersSecond):
        self.cruiseMetersSecond = cruiseMetersSecond
    def getCruiseHeight(self):
        return self.cruiseMetersSecond
    def setCruiseHeight(self, cruiseHeight):
        self.cruiseHeight = cruiseHeight


    def __str__(self):
        return 'upHeight:{0}\n' \
               'cruiseMetersSecond:{1}\n' \
               'cruiseHeight:{2}'.format(self.getUpHeight(),
                                     self.getCruiseMetersSecond(),
                                     self.getCruiseHeight())


if __name__ == '__main__':
    info = BadaInfo('AircraftConfig.yml')
    print info