from blesensor import BLESensor
import time
import sys
import os


try:
    DISTANCE_SENSOR = os.environ['DISTANCE_SENSOR']
    DISTANCE_SENSOR_2 = os.environ['DISTANCE_SENSOR_2']
    DISTANCE_SERVICE = os.environ['DISTANCE_SERVICE']
except KeyError as e:
    sys.exit('Couldn\'t find env: {}'.format(e))

sensors = [
    {'addr': DISTANCE_SENSOR, 'svc': DISTANCE_SERVICE}
    {'addr': DISTANCE_SENSOR_2, 'svc': DISTANCE_SERVICE}
]

sensorObjs = []
for sensor in sensors:
    sensorObjs.append(BLESensor(sensor['addr'], sensor['svc']))

[ i.start() for i in sensorObjs ]

try:
    while True:
        for i in sensorObjs:
            print("Sensor {0} : {1}".format(i.addr, i.state))
            time.sleep(1)

except KeyboardInterrupt:
    [ i.join() for i in sensorObjs ]
    sys.exit(0)
