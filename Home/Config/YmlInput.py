# coding=utf-8

'''
    author: V0
    date: 2021/12/01
'''

import yaml
import os

class YmlInput(object):
    # 获取当前文件所在文件夹路径
    ymlPath = ''
    dicData = {}
    def __init__(self,fileName,filePath = os.path.dirname(os.path.dirname(__file__) + os.path.sep + 'yaml' + os.path.sep)):
        #print filePath
        assert(os.path.exists(filePath + os.path.sep + fileName)), 'Not find ' + fileName
        self.ymlPath = os.path.join(filePath, fileName)  # 获取yaml文件路径
        #打开文件
        f = open(self.ymlPath, 'r')
        cfg = f.read()
        self.dicData = yaml.safe_load(cfg)  # 用load方法转字典
        f.close()
    #返回字典数据
    def getDicData(self):
        return self.dicData
    #当前字典返回配置文件
    def setYmlFile(self):
        f = open(self.ymlPath, 'w')
        yaml.dump(self.dicData, f)
        f.close()


if __name__ == '__main__':
    input = YmlInput('info.yml')
    data = input.getDicData()
    for key in data:
        print key,':',data[key], type(data[key])
        #data[key] = '123'
    input.setYmlFile()