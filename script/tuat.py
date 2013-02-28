import hrp
import hstsetup

from hrp import *

motionId = 25
motions = {
    1:  "myrand",
    2:  "walk_forward",
    3:  "walk_right",
    4:  "walk_left",
    5:  "step",
    6:  "squat",
    7:  "tilt_front",
    8:  "tilt_right",
    9:  "tilt_cross",
    10: "myrand2",
    11: "myrand3",
    12: "myrand4",
    13: "myrand5",
    14: "step_walk",
    15: "tilt1",
    16: "tilt2",
    17: "tilt3",
    18: "tilt4",
    19: "tilt5",
    20: "tilt6",
    21: "manual_right_roll",
    22: "manual_left_roll",
    23: "manual_right_pitch",
    24: "manual_left_pitch",
    25: "manual_both_pitch",
    }

if not motions.has_key(motionId):
    print("bad motion id")
    raise

ms = findPluginManager("motionsys")
ms.load("kfplugin")
kf = ms.create("kfplugin","kf","")
ms.load("seqplay")
seq = SequencePlayerHelper.narrow(ms.create("seqplay","seq",""))
ms.load("hstabilizer")
st = ms.create("hstabilizer","st","")
ms.load("logplugin")
log = LoggerPluginHelper.narrow(ms.create("logplugin","log",""))
seq.start()
# Resize logger buffer to properly store longuer sequences.
log.sendMsg(":max-length 10000")
log.add("kf")
log.start()
seq.goHalfSitting(3)
seq.waitInterpolation()
hstsetup.stsetup(st)
kf.start()
st.start()
waitInputConfirm("put the robot down. start walking")
seq.loadPattern("../etc/tuat/%(1)d.%(2)s/%(2)s" \
                    % {'1': motionId, '2': motions[motionId]},
                1.0)
seq.waitInterpolation()
log.stop()
log.save("tuat")
print("saved")
