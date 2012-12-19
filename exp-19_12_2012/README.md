retrieve-logs copy the logs from the robot to the current directory.

plot-graphs take all the astate and rstate data and draw each
column in a separate file. 151-156 are accelerometers information,
see the script for more info.

WARNING: generated tuat-{a,r}state.log file headers are *wrong*.
Column number does not match as some rotations are expressed using
rotation matrices (9 columns) instead of quaternions.
