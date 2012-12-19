import hrp
import hstsetup

from hrp import *

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
log.add("kf")
log.start()
seq.goHalfSitting(3)
seq.waitInterpolation()
pose=[0,2.1926e-009,-0.4538,0.8727,-0.4189,-2.1926e-009,-0,-2.1926e-009,-0.4538,0.8727,-0.4189,2.1926e-009,0,0,0,0,0.2618,-0.1745,0,-0.5236,0,0,0,0,0.2618,0.1745,0,-0.5236,0,0,0,0,-0,0,-0,0,-0,-0,0,-0,0,-0]
#seq.getReferenceState(pose)
pose[17] = -1.45
pose[25] = 1.45
seq.setJointAngles(pose, 5.)
seq.waitInterpolation()
hstsetup.stsetup(st)
kf.start()
st.start()
waitInputConfirm("put the robot down. start walking")
waitInputConfirm("stop logging")
log.stop()
log.save("tuat")
print("saved")

