#create the array to hold the rule set
import numpy as np
'''removed np array init'''

#define rules
rules[20,20,1,0,0]=1
#general persists
rules[20,1,0,0,0]=3
rules[1,0,0,0,0]=4#fast wave
rules[0,0,0,0,0]=0#no instantaneous change from quiescent
rules[0,0,0,0,20]=0
#no instantaneous change from quiescent
rules[0,0,0,20,20]=0#no instantaneous change from quiescent
rules[20,20,1,3,4]=1#general persists
rules[20,1,3,4,0]=7
#start slow wave
rules[1,3,4,0,0]=4
rules[3,4,0,0,0]=3
rules[4,0,0,0,0]=4
#fast wave
rules[20,20,1,7,4]=1
#general persists
rules[20,1,7,4,3]=3
rules[1,7,4,3,4]=7
#slow wave
rules[7,4,3,4,0]=3
rules[4,3,4,0,0]=4
rules[20,20,1,3,7]=1
#general persists
rules[20,1,3,7,3]=3
rules[1,3,7,3,4]=4#fast wave
rules[3,7,3,4,3]=6#slow wave
rules[7,3,4,3,4]=4
rules[3,4,3,4,0]=3
rules[20,1,3,4,6]=7 #slow wave
rules[1,3,4,6,4]=3
rules[3,4,6,4,3]=7 #slow wave
rules[4,6,4,3,4]=4
rules[6,4,3,4,3]=3
rules[4,3,4,3,4]=4
rules[20,1,7,3,7]=7 #slow wave
rules[1,7,3,7,4]=4
#fast wave
rules[7,3,7,4,3]=3
rules[3,7,4,3,4]=7
#slow wave
rules[7,4,3,4,3]=3
rules[3,4,3,4,3]=3
rules[1,7,4,3,7]=6
#slow wave
rules[7,4,3,7,3]=3
rules[4,3,7,3,4]=4
#fast wave
rules[3,4,0,0,20]=3
rules[4,0,0,20,20]=1#fast wave hits far end
rules[20,20,1,3,6]=1#general persists
rules[20,1,3,6,3]=3
rules[1,3,6,3,4]=7
rules[3,6,3,4,6]=3
rules[6,3,4,6,4]=3
rules[4,3,4,3,1]=5
#fast reverse wave
rules[3,4,3,1,20]=0
rules[4,3,1,20,20]=1
rules[1,3,7,3,3]=7
#general persists
#slow wave
rules[3,7,3,3,7]=3
rules[7,3,3,7,4]=4
rules[3,3,7,4,3]=3
rules[7,3,4,3,7]=3
rules[3,4,3,7,3]=3
rules[7,3,4,3,5]=5
#fast reverse wave
rules[4,3,5,0,5]=5
rules[3,5,0,5,7]=0
rules[5,0,5,7,1]=7
rules[0,5,7,1,20]=0
rules[5,7,1,20,20]=1
#general persists
rules[1,3,4,6,3]=3
rules[3,4,6,3,3]=6#slow wave
rules[4,6,3,3,4]=4#fast wave
rules[6,3,3,4,6]=3
rules[3,3,4,6,5]=5#fast reverse wave
rules[3,4,6,5,0]=1#intersection of reverse fast and forward slow waves
rules[4,6,5,0,5]=4#fast wave
rules[6,5,0,5,0]=0
rules[5,0,5,0,7]=5
rules[0,5,0,7,0]=6
rules[5,0,7,0,1]=5
#fast reverse wave
rules[0,7,0,1,20]=0
rules[7,0,1,20,20]=1#general persists
rules[20,20,1,7,3]=1#general persists
rules[20,1,7,3,6]=7
#slow wave
rules[1,7,3,6,4]=3
rules[7,3,6,4,3]=7#slow wave
rules[3,6,4,3,5]=7#slow wave
rules[6,4,3,5,1]=0
rules[4,3,5,1,4]=7#slow wave
rules[3,5,1,4,0]=1#general persists
rules[5,1,4,0,5]=7#slow wave
rules[1,4,0,5,6]=3
rules[4,0,5,6,5]=7#slow wave
rules[0,5,6,5,0]=7#slow wave
rules[5,6,5,0,1]=0
rules[6,5,0,1,20]=7
rules[4,3,4,3,5]=5
#fast reverse wave
rules[3,4,3,5,0]=0
rules[4,3,5,0,1]=5
rules[3,5,0,1,20]=7
#slow wave
rules[5,0,1,20,20]=1
#general persists
rules[1,7,3,7,7]=7
rules[7,3,7,7,0]=1
rules[3,7,7,0,7]=1
rules[7,7,0,7,1]=7
rules[7,0,7,1,7]=7
rules[0,7,1,7,3]=1
#general persists
rules[7,1,7,3,7]=7
rules[7,0,7,1,20]=7
rules[0,7,1,20,20]=1
#general persists
rules[20,20,1,7,7]=2
rules[20,1,7,7,1]=2
rules[1,7,7,1,1]=2
rules[7,7,1,1,7]=2
rules[7,1,1,7,7]=2
rules[1,1,7,7,1]=2
rules[1,7,7,1,7]=2
rules[7,7,1,7,7]=2
rules[7,1,7,7,1]=2
rules[1,7,7,1,20]=2
rules[7,7,1,20,20]=2
rules[1,7,4,3,1]=1
#intersection of waves
rules[7,4,3,1,20]=0
rules[20,20,1,3,1]=2
rules[20,1,3,1,0]=2
rules[1,3,1,0,1]=2
rules[3,1,0,1,20]=2
rules[1,0,1,20,20]=2
rules[7,3,4,3,1]=5
rules[1,3,4,6,5]=7
rules[4,6,5,0,1]=7
rules[3,7,4,3,5]=1
#intersection of waves
rules[7,4,3,5,0]=0
rules[7,4,3,1,0]=0
rules[4,3,1,0,5]=1
#general persists
rules[3,1,0,5,7]=3
rules[1,0,5,7,1]=1
rules[3,1,0,1,3]=2
rules[1,0,1,3,1]=2
rules[0,1,3,1,0]=2
rules[6,3,4,6,5]=5
rules[6,5,0,5,7]=0
rules[1,3,7,3,5]=1
rules[3,7,3,5,1]=1
rules[7,3,5,1,4]=0
rules[5,1,4,0,7]=3
rules[1,4,0,7,0]=1
rules[4,0,7,0,1]=1
rules[20,1,3,1,1]=2
rules[1,3,1,1,0]=2
rules[3,1,1,0,1]=2
rules[1,1,0,1,3]=2
rules[0,1,3,1,1]=2
rules[1,1,0,1,20]=2
rules[3,4,3,1,0]=0
rules[3,1,0,5,0]=3
rules[1,0,5,0,7]=4
rules[6,5,0,1,3]=7
rules[5,0,1,3,4]=1
rules[0,1,3,4,6]=7
rules[20,1,0,0,20]=3
rules[1,0,0,20,20]=1
rules[20,1,3,1,20]=2
rules[1,3,1,20,20]=2
rules[3,3,4,6,4]=3
rules[3,6,4,3,3]=3
rules[6,4,3,3,7]=3
rules[4,3,3,7,4]=4
rules[3,5,0,5,0]=0
rules[1,7,3,7,3]=3
rules[7,3,7,3,3]=7
rules[3,7,3,3,4]=4
rules[7,3,3,4,3]=3
rules[3,3,4,3,1]=5
rules[1,0,5,0,5]=4
rules[0,5,0,5,6]=0
rules[5,0,5,6,5]=5
rules[3,5,0,1,3]=7
rules[0,1,3,4,0]=7
rules[1,3,4,0,5]=4
rules[3,4,0,5,7]=3
rules[4,0,5,7,0]=1
#intersection
rules[0,5,7,0,7]=0
rules[5,7,0,7,1]=5
rules[0,5,7,1,7]=0
rules[5,7,1,7,4]=1
#general persists
rules[7,1,7,4,3]=3
rules[3,3,4,3,7]=3
rules[3,7,4,3,3]=6
rules[7,4,3,3,3]=3
rules[4,3,3,3,4]=4
rules[3,3,3,4,6]=3
rules[5,0,5,0,5]=5
rules[1,7,4,3,6]=6
rules[7,4,3,6,3]=3
rules[4,3,6,3,4]=7
rules[3,6,3,4,3]=3
rules[6,3,4,3,5]=5
rules[3,4,3,5,1]=0
rules[1,4,0,5,0]=3
rules[4,0,5,0,5]=4
rules[0,5,0,5,7]=0
rules[5,0,5,7,0]=7
rules[1,3,6,3,7]=6
rules[3,6,3,7,3]=3
rules[6,3,7,3,5]=1#intersection
rules[3,7,3,5,0]=1#intersection
rules[7,3,5,0,7]=0
rules[3,5,0,7,1]=6
rules[5,0,7,1,7]=0
rules[7,1,7,3,4]=3
rules[1,7,3,4,0]=6
rules[7,3,4,0,7]=3
rules[3,4,0,7,0]=1#intersection
rules[4,0,7,0,5]=1#intersection
rules[0,7,0,5,7]=0
rules[7,0,5,7,1]=6
rules[1,3,6,3,1]=1
#intersection
rules[3,6,3,1,1]=0
rules[6,3,1,1,0]=1#general persists
rules[3,1,1,0,6]=1#general persists
rules[1,1,0,6,0]=3
rules[1,0,6,0,1]=1
#intersection
rules[0,6,0,1,3]=0
rules[6,0,1,3,6]=1
#general persists
rules[0,1,3,6,3]=3
rules[0,6,0,1,20]=0
rules[6,0,1,20,20]=1
#general persists
rules[3,1,0,1,1]=2
rules[1,0,1,1,3]=2
rules[0,1,1,3,1]=2
rules[1,1,3,1,0]=2
rules[6,3,4,3,3]=3
rules[3,4,3,3,7]=3
rules[6,3,7,3,3]=7
rules[3,7,3,3,3]=3
rules[7,3,3,3,4]=4
rules[3,3,3,4,3]=3
rules[0,5,0,5,0]=0
rules[6,3,7,3,4]=4
rules[3,4,0,5,0]=3
rules[4,0,5,0,7]=4
rules[5,0,7,0,5]=5
rules[7,4,3,4,6]=3
rules[4,3,4,6,5]=5
rules[4,6,5,0,6]=4
rules[6,5,0,6,0]=0
rules[5,0,6,0,1]=7
rules[0,7,0,1,3]=0
rules[0,1,3,7,3]=3
rules[7,0,1,3,7]=1
rules[7,3,4,3,3]=3
rules[3,4,3,3,3]=3
rules[6,3,4,6,3]=3
rules[6,3,3,4,3]=3
rules[3,3,4,3,5]=5
rules[3,7,3,3,6]=3
rules[7,3,3,6,4]=3
rules[3,3,6,4,3]=7
rules[4,3,5,0,7]=5
rules[6,4,3,5,0]=0
rules[7,3,4,0,5]=4
rules[3,4,0,5,6]=3
rules[5,6,5,0,6]=0
rules[7,3,3,7,7]=5
rules[3,3,7,7,0]=1
rules[3,7,7,0,5]=1
rules[7,7,0,5,6]=4
rules[7,0,5,6,0]=0
rules[0,5,6,0,1]=7
rules[5,6,0,1,3]=0
rules[0,1,3,6,4]=3
rules[1,3,6,4,3]=7
rules[3,6,4,3,7]=3
rules[6,4,3,7,7]=5
rules[4,3,7,7,0]=1
rules[3,7,7,0,0]=1
rules[7,7,0,0,7]=4
rules[0,0,7,0,1]=7
rules[7,0,0,7,0]=0
rules[7,3,5,1,1]=0
rules[1,1,4,0,7]=3
rules[3,5,1,1,4]=1
rules[5,1,1,4,0]=1
rules[1,1,3,1,1]=2
rules[1,1,0,1,1]=2
rules[6,4,3,3,3]=3
rules[3,3,4,3,3]=3
rules[3,3,7,3,3]=7
rules[7,3,3,7,3]=3
rules[5,7,0,0,7]=5
rules[4,3,4,0,5]=4
rules[0,5,7,0,0]=0
rules[7,3,4,3,6]=3
rules[3,4,3,6,3]=3
rules[4,6,3,3,7]=3
rules[6,3,3,7,3]=3
rules[0,7,0,5,0]=0
rules[7,0,5,0,7]=0
rules[7,3,5,0,5]=0
rules[3,5,0,5,6]=0
rules[5,0,5,6,0]=5
rules[3,3,7,3,5]=1
rules[3,6,4,3,4]=4
rules[6,4,3,4,0]=3
rules[4,3,4,0,7]=3
rules[1,7,3,6,3]=3
rules[7,3,6,3,3]=6
rules[3,6,3,3,1]=5
rules[6,3,3,1,1]=0
rules[3,3,1,1,0]=1
rules[3,1,1,0,0]=1
rules[1,0,0,5,7]=4
rules[0,0,5,7,0]=6
rules[0,5,7,0,1]=0
rules[5,7,0,1,3]=7
rules[1,1,0,0,5]=3
rules[0,1,3,7,4]=7
rules[1,3,7,4,3]=3
rules[7,4,3,3,1]=5
rules[4,3,3,1,1]=0
rules[1,1,0,0,6]=3
rules[1,0,0,6,5]=4
rules[0,0,6,5,0]=6
rules[0,6,5,0,1]=0
rules[1,7,3,6,5]=7
rules[7,3,6,5,0]=1
rules[3,6,5,0,1]=7
rules[6,5,0,1,1]=7
rules[5,0,1,1,3]=1
rules[0,1,1,3,4]=1
rules[1,1,3,4,6]=7
rules[1,3,4,6,0]=7
rules[6,0,7,1,7]=7
rules[3,4,6,0,7]=1
rules[4,6,0,7,1]=7
rules[6,0,7,1,20]=7
rules[7,1,7,3,6]=7
rules[3,6,3,3,7]=3
rules[3,3,7,3,4]=4
rules[5,0,0,6,5]=5
rules[6,5,0,0,6]=0
rules[4,6,5,0,0]=4
rules[3,6,3,3,4]=4
rules[3,4,3,4,6]=3
rules[5,6,0,7,1]=0
rules[0,5,6,0,7]=7
rules[4,0,5,6,0]=7
rules[4,6,4,3,5]=7
rules[3,3,4,6,3]=3
rules[5,6,5,0,0]=0
rules[6,4,3,3,6]=3
rules[4,3,3,6,4]=3
rules[7,3,3,3,7]=3
rules[3,3,3,7,7]=5
rules[7,7,0,5,0]=4
rules[7,0,5,0,5]=0
rules[3,4,3,7,7]=5
rules[0,0,5,6,0]=0
rules[7,0,0,5,6]=0
rules[7,7,0,0,5]=4
rules[4,3,4,3,7]=3
rules[7,3,3,5,1]=0
rules[0,7,0,7,1]=0
rules[1,4,0,0,7]=3
rules[0,0,7,0,7]=7
rules[4,0,0,7,0]=7
rules[1,1,4,0,0]=7
rules[3,7,3,3,5]=7
rules[3,3,5,1,1]=7
rules[7,0,7,1,1]=7
rules[7,1,1,7,3]=1
rules[0,7,1,1,7]=1
rules[1,1,7,3,7]=7
rules[3,3,3,7,3]=3
rules[3,3,3,7,4]=4
rules[5,7,0,0,5]=5
rules[1,0,5,0,0]=4
rules[0,5,0,0,7]=0
rules[5,0,0,7,0]=5
rules[3,3,4,3,6]=3
rules[4,3,3,3,7]=3
rules[7,0,5,0,0]=0
rules[6,3,3,3,1]=5
rules[3,3,3,1,1]=0
rules[0,0,0,5,7]=0
rules[1,0,0,0,5]=4
rules[1,1,0,0,0]=3
rules[4,3,6,3,3]=6
rules[3,6,3,3,3]=3
rules[1,0,0,5,0]=4
rules[0,0,5,0,7]=0
rules[5,0,7,0,7]=5
rules[7,3,7,3,4]=4
rules[3,4,3,3,1]=5
rules[1,3,6,3,6]=6
rules[3,6,3,6,3]=3
rules[3,6,3,5,0]=0
rules[6,3,5,0,1]=5
rules[3,5,0,1,1]=7
rules[6,3,6,3,5]=1
rules[6,0,5,7,1]=6
rules[0,6,0,5,7]=0
rules[1,1,3,4,0]=7
rules[1,3,4,0,6]=4
rules[3,4,0,6,5]=3
rules[4,0,6,0,5]=1
rules[3,4,0,6,0]=3
rules[4,0,6,5,0]=1
rules[6,5,0,7,1]=6
rules[0,6,5,0,7]=0
rules[1,7,3,4,6]=6
rules[7,3,4,6,3]=3
rules[3,4,6,3,5]=1
rules[4,6,3,5,0]=0
rules[3,6,3,1,0]=0
rules[3,1,0,6,0]=3
rules[6,3,1,0,5]=1
rules[4,3,1,0,6]=1
rules[0,5,7,1,1]=0
rules[7,1,1,7,4]=1
rules[1,1,7,4,3]=3
rules[5,7,1,1,7]=1
rules[6,3,3,3,7]=3
rules[6,3,6,3,3]=6
rules[6,3,3,3,4]=4
rules[6,5,0,0,0]=0
rules[5,0,0,0,5]=5
rules[6,3,6,3,4]=7
rules[4,0,5,0,6]=4
rules[5,0,6,0,5]=7
rules[0,5,0,6,0]=0
rules[4,3,7,3,5]=1
rules[7,0,6,0,1]=6
rules[0,7,0,6,0]=0
rules[4,0,7,0,6]=1
rules[3,4,3,3,6]=3
rules[7,3,3,3,3]=3
rules[3,3,3,3,7]=3
rules[7,0,0,5,0]=0
rules[0,0,5,0,6]=0
rules[7,3,3,3,5]=5
rules[3,3,3,5,1]=0
rules[1,4,0,0,5]=3
rules[4,0,0,5,6]=4
rules[0,0,5,6,5]=0
rules[5,6,5,0,7]=0
rules[7,3,4,6,4]=3
rules[4,6,4,3,3]=3
rules[6,4,3,3,5]=5
rules[4,3,3,5,1]=0
rules[1,4,0,0,0]=3
rules[4,0,0,0,7]=4
rules[0,0,7,0,6]=7
rules[0,0,0,7,0]=0
rules[5,0,7,1,1]=0
rules[1,1,7,3,4]=3
rules[0,6,0,1,1]=0
rules[6,0,1,1,3]=1
rules[1,1,3,6,3]=3
rules[0,1,1,3,6]=1
rules[5,0,0,0,7]=5
rules[0,5,0,0,0]=0
rules[5,0,7,0,6]=5
rules[4,6,3,3,3]=3
rules[6,3,3,3,3]=3
rules[3,3,3,3,1]=5
rules[0,0,5,0,5]=0
rules[4,3,4,3,3]=3
rules[0,0,0,5,0]=0
rules[3,3,6,3,3]=6
rules[7,3,3,6,3]=3
rules[6,3,3,5,0]=0
rules[3,3,5,0,1]=5
rules[3,6,3,3,5]=5
rules[3,4,0,0,5]=3
rules[4,0,0,5,7]=4
rules[0,5,7,0,6]=0
rules[5,7,0,6,0]=5
rules[3,6,3,7,4]=4
rules[6,3,7,4,3]=3
rules[4,3,3,5,0]=0
rules[7,4,3,3,5]=5
rules[3,4,0,0,6]=3
rules[4,0,0,6,5]=4
rules[0,6,5,0,6]=0
rules[7,3,3,6,5]=5
rules[3,3,6,5,0]=1
rules[3,6,5,0,5]=4
rules[4,3,4,6,0]=5
rules[3,4,6,0,5]=1
rules[4,6,0,5,6]=4
rules[6,0,5,6,0]=0
rules[3,6,4,3,6]=3
rules[6,4,3,6,5]=5
rules[4,3,6,5,0]=1
rules[3,4,6,0,0]=1
rules[4,6,0,0,7]=4
rules[6,0,0,7,0]=0
rules[0,7,0,1,1]=0
rules[1,1,3,7,3]=3
rules[7,0,1,1,3]=1
rules[0,1,1,3,7]=1
rules[3,3,3,3,4]=4
rules[4,0,5,0,0]=4
rules[0,5,0,0,6]=0
rules[0,5,6,0,0]=7
rules[5,6,0,0,7]=0
rules[4,3,3,3,3]=3
rules[0,0,5,0,0]=0
rules[3,3,3,3,5]=5
rules[4,0,0,5,0]=4
rules[3,4,3,3,5]=5
rules[4,0,0,0,5]=4
rules[0,0,0,5,6]=0
rules[7,3,3,5,0]=0
rules[3,3,5,0,7]=5
rules[7,3,4,0,0]=4
rules[3,4,0,0,7]=3
rules[0,0,7,0,5]=7
rules[0,7,0,5,6]=0
rules[6,4,3,7,3]=3
rules[4,3,7,3,3]=7
rules[0,7,0,0,7]=0
rules[0,0,7,0,0]=7
rules[5,6,0,1,1]=0
rules[1,1,3,6,4]=3
rules[3,3,3,3,3]=3
rules[6,3,3,3,5]=5
rules[3,3,3,5,0]=0
rules[4,6,3,3,6]=3
rules[6,3,3,6,3]=3
rules[3,3,6,3,5]=1
rules[6,3,5,0,5]=5
rules[4,3,4,0,6]=4
rules[0,6,0,5,0]=0
rules[6,0,5,0,7]=0
rules[0,6,5,0,0]=0
rules[6,5,0,0,7]=0
rules[7,3,3,4,6]=3
rules[6,3,3,1,0]=0
rules[3,3,1,0,5]=1
rules[4,3,1,0,0]=1
rules[3,1,0,0,5]=3
rules[4,3,3,1,0]=0
rules[3,1,0,0,6]=3
rules[3,3,6,3,4]=7
rules[3,6,3,3,6]=3
rules[0,7,0,0,6]=0
rules[7,0,0,6,5]=0
rules[4,0,7,0,0]=1
rules[4,6,3,3,1]=5
rules[1,0,0,6,0]=4
rules[0,0,6,0,7]=6
rules[0,6,0,7,1]=0
rules[0,7,0,0,5]=0
rules[7,0,0,5,7]=0
rules[7,4,3,3,7]=3
rules[4,3,3,7,3]=3
rules[7,0,0,6,0]=0
rules[5,7,0,1,1]=7
rules[1,1,3,7,4]=7
rules[6,0,7,1,1]=7
rules[1,1,7,3,6]=7
rules[5,0,7,0,0]=5
rules[5,0,0,6,0]=5
rules[4,3,3,6,3]=3
rules[3,3,5,0,5]=5
rules[7,3,3,3,6]=3
rules[3,3,3,6,5]=5
rules[5,0,6,0,7]=7
rules[4,6,0,5,0]=4
rules[6,0,5,0,6]=0
rules[3,4,3,6,5]=5
rules[7,3,6,3,4]=7
rules[6,3,4,3,6]=3
rules[4,6,0,0,5]=4
rules[6,0,0,5,6]=0
rules[3,3,5,1,4]=7
rules[5,1,4,0,0]=7
rules[3,3,3,6,3]=3
rules[3,3,3,6,4]=3
rules[5,6,0,0,5]=0
rules[4,3,3,7,7]=5
rules[7,7,0,0,0]=4
rules[7,0,0,0,7]=0
rules[7,0,5,0,6]=0
rules[6,3,4,3,7]=3
rules[0,7,0,0,0]=0
rules[5,7,0,0,0]=5
rules[4,3,3,3,6]=3
rules[6,0,5,0,0]=0
rules[3,3,3,1,0]=0
rules[3,1,0,0,0]=3
rules[6,3,3,3,6]=3
rules[7,0,0,0,5]=0
rules[4,3,3,3,1]=5
rules[1,0,0,0,6]=4
rules[0,0,0,6,0]=0
rules[0,0,6,0,5]=6
rules[4,3,6,3,5]=1
rules[4,0,6,0,6]=1
rules[6,0,6,0,1]=6
rules[0,6,0,6,0]=0
rules[7,0,0,0,6]=0
rules[0,0,0,6,5]=0
rules[0,0,6,0,6]=6
rules[5,0,0,0,6]=5
rules[5,0,6,0,6]=7
rules[3,3,3,3,6]=3
rules[6,0,0,5,0]=0
rules[0,5,6,0,6]=7
rules[5,6,0,6,0]=0
rules[6,3,6,4,3]=7
rules[3,6,3,6,4]=3
rules[7,0,0,0,0]=0
rules[0,0,0,0,7]=0
rules[0,0,0,0,6]=0
rules[4,6,3,3,5]=5
rules[4,0,0,6,0]=4
rules[0,0,6,0,0]=6
rules[0,6,0,0,7]=0
rules[0,0,0,0,5]=0
rules[0,6,0,5,6]=0
rules[6,4,3,6,3]=3
rules[5,0,0,0,0]=5
rules[4,3,3,3,5]=5
rules[4,0,0,0,6]=4
rules[4,0,6,0,0]=1
rules[0,6,0,0,6]=0
rules[6,0,0,6,5]=0
rules[0,6,0,0,5]=0
rules[6,0,0,5,7]=0
rules[7,4,3,3,6]=3
rules[6,0,0,6,0]=0
rules[5,0,6,0,0]=7
rules[5,7,0,0,6]=5
rules[6,3,3,7,4]=4
rules[4,3,3,6,5]=5
rules[4,6,0,0,0]=4
rules[6,0,0,0,7]=0
rules[0,6,0,0,0]=0
rules[5,6,0,0,0]=0
rules[6,0,0,0,5]=0
rules[6,0,0,0,6]=0
rules[6,0,0,0,0]=0
rules[5,6,0,0,6]=0
rules[6,3,3,6,4]=3
#even rules here
rules[20,20,1,0,20]=2
rules[20,1,0,20,20]=2
rules[1,0,0,0,20]=4
rules[1,3,4,0,20]=7
rules[3,4,0,20,20]=1
rules[4,0,0,0,20]=4
rules[4,3,4,0,20]=5
rules[7,3,5,1,20]=0
rules[3,5,1,20,20]=1
rules[4,3,5,1,20]=7
rules[5,0,7,1,20]=0
rules[5,6,0,1,20]=0
rules[5,7,0,1,20]=7