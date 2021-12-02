# coding=utf-8
from CsvOutputFile import CsvOutput
import math

def util(flightPath):
    arr = []
    data = flightPath.aircraft.StateVector.aircraftStateHistory
    index = 0
    # 航向角
    yawAngle = flightPath.finalRoute.TailHeadDegrees
    # 滚转角
    rollAngle = flightPath.aircraft.TurnCourse
    csvdata = []
    for vertice in flightPath.finalRoute.getVertices():
        # 获取时间
        t = vertice.getWeight().getElapsedTimeSeconds()
        # 获取名字
        name = vertice.getWeight().getName()
        # 获取经度
        Longitude = vertice.getWeight().getLongitudeDegrees()
        # 获取纬度
        Latitude = vertice.getWeight().getLatitudeDegrees()
        # 获取海拔高度
       # Altitude = vertice.getWeight().getAltitudeMeanSeaLevelMeters()

        if index < len(data) and index < len(yawAngle) and index < len(rollAngle):
            if index + 1 < len(yawAngle) and rollAngle[index] != 0 and (yawAngle[index + 1] - yawAngle[index] < 0 or \
                    yawAngle[index + 1] - yawAngle[index] > 180):
                rollAngle[index] *= -1
            da = data[index].values()
            #                                         海拔高度    真空速度    质量      俯仰角        航向角          滚转角
            arr.append([t, name, Longitude, Latitude, da[0][0], da[0][1], da[0][4], da[0][5], yawAngle[index], rollAngle[index]])
            #
            csvdata.append([t, Longitude, Latitude, da[0][0], rollAngle[index], da[0][5], yawAngle[index]])
        index += 1

    #滚转角处理
    Finalnum = 562
    RollPerSecond = 3.0
    deltaTimeSeconds = flightPath.deltaTimeSeconds
    deltaPerSecond = deltaTimeSeconds * RollPerSecond
    i = 0
    while i < len(arr):
        left = i
        while i < len(arr) - 1 and arr[i][9] != 0:
            i += 1
        right = i
        rollMax = 0.0
        isval = 1
        if left != right:
            deltaYaw = arr[right][8] - arr[left][8]
            if deltaYaw > 180:
                deltaYaw -= 360
            elif deltaYaw < -180:
                deltaYaw += 360
            rollMax = math.degrees(math.atan(deltaYaw * ((arr[right][5] + arr[left][5]) / 2.0) / Finalnum / (arr[right][0] - arr[left][0])))
            if rollMax < 0:
                isval *= -1
        while rollMax != 0 and left <= right:
            arr[left][9] =  (arr[left - 1][9] if left > 0  else 0) + isval * deltaPerSecond
            arr[right][9] =  (arr[right + 1][9] if right + 1 < len(arr)  else 0) + isval * deltaPerSecond
            if rollMax > 0 and arr[left][9] > rollMax or rollMax < 0 and arr[left][9] < rollMax:
                arr[left][9] = rollMax
            if  rollMax > 0 and arr[right][9] > rollMax or rollMax < 0 and arr[right][9] < rollMax:
                arr[right][9] = rollMax
            csvdata[left][4] =  arr[left][9]
            csvdata[right][4] =  arr[right][9]
            left += 1
            right -= 1
        i += 1

    filePrefix = ''
    if not (flightPath.departureAirport is None):
        filePrefix = flightPath.departureAirport.getICAOcode()
        if not (flightPath.arrivalAirport is None):
            filePrefix += '-' + flightPath.arrivalAirport.getICAOcode()
    # 文件名称
    fileName = filePrefix

    handers = ['Time',
                'Longitude  ',
                'Latitude',
                'Altitude',
                'Roll (deg)',
                'Pitch (deg)',
                'Yaw (deg)'
                ]
    csvOutput = CsvOutput(fileName, handers, csvdata)


if __name__ == '__main__':
    pass