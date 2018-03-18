################################################################################
# Copyright (C) 2012-2016 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################


#line 34 change writeheader  in case of append to False

import Leap, sys, time, csv,os
import string
import pandas as pd
from Leap import ScreenTapGesture
import numpy as np
from decimal import Decimal
from collections import OrderedDict
from predict import *
L=5


class SampleListener(Leap.Listener):
            finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
            bone_names = ['M', 'P', 'I', 'D']
            state_names = ["STATE INVALID", "STATE START","STATE END","STATE UPDATE"]
            global fieldnames
            global writeheaders
            global second_iteration
            global start_time
            global elapsed
            global ges_type,si,gate ,d
            d=pd.DataFrame(dtype=float)
            gate=True
            second_iteration = False
            writeheaders = True
            elapsed = 0
            start_time = 0
            fieldnames = [
                          'R.Thumb.TTP','R.Index.TTP','R.Middle.TTP','R.Ring.TTP','R.Pinky.TTP',
                          'L.Thumb.TTP','L.Index.TTP','L.Middle.TTP','L.Ring.TTP','L.Pinky.TTP',
                          'R.Thumb.TNA', 'R.Index.TNA', 'R.Middle.TNA', 'R.Ring.TNA', 'R.Pinky.TNA', 'L.Thumb.TNA',
                          'L.Index.TNA', 'L.Middle.TNA', 'L.Ring.TNA', 'L.Pinky.TNA',
                          'R.Thumb_Index.ang', 'R.Index_Middle.ang', 'R.Middle_Ring.ang', 'R.Ring_Pinky.ang',
                          'L.Thumb_Index.ang', 'L.Index_Middle.ang', 'L.Middle_Ring.ang', 'L.Ring_Pinky.ang',


                          ]


                # run only once per file then make it comment


            def on_init(self, controller):
                     print(" Initialized ")

            def on_connect(self, controller):
                     print(" Connected ")
                     controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)

            def on_disconnect(self, controller):
                      # Note: not dispatched when running in a debugger.
                     print(" Disconnected ")

            def on_exit(self, controller):
                print(" Exited ")

            LastFrameID = 0

            def processFrame(self, frame):
                if frame.id == self.LastFrameID:
                          return
                self.LastFrameID = frame.id

            def on_frame(self, controller):
                    # Get the most recent frame and report some basic information
                    global writeheaders
                    global second_iteration
                    global start_time
                    global elapsed,gate,d


                    cach_dict = OrderedDict((key, 0) for  key in fieldnames)


                    frame = controller.frame()
                        #for gesture in frame.gestures():
                    gesture=frame.gestures()
                    if (gesture[0].type == Leap.Gesture.TYPE_KEY_TAP or second_iteration):

                                if(second_iteration==False):
                                    print("START recording AFTER:")
                                    for x in range(1,4,1):
                                        print(x)
                                        time.sleep(1)
                                        if(x==3):
                                            print ("RECORDING")
                                            print ("\n")
                                            print ("\n")
                                    second_iteration = True

                                if (len(frame.hands) <= 2) and (len(frame.hands)!= 0):
                                    total_speed = []


                                    #cach_dict.update({"Frame id" : str(frame.id) , "timestamp" : str(frame.timestamp) , "hands" : str(len(frame.hands)) ,"fingers" : str(len(frame.fingers))})



                                    for hand in frame.hands:
                                        # 0 for right hand and 1 for left
                                        handType = "L" if hand.is_left else "R"
                                        hand_x_basis = hand.basis.x_basis
                                        hand_y_basis = hand.basis.y_basis
                                        hand_z_basis = hand.basis.z_basis
                                        hand_origin = hand.palm_position
                                        hand_transform = Leap.Matrix(hand_x_basis, hand_y_basis, hand_z_basis,
                                                                     hand_origin)
                                        hand_transform = hand_transform.rigid_inverse()

                                        normal = hand.palm_normal
                                        direction = hand.direction

                                        arm = hand.arm

                                        sphere=hand.sphere_center


                                        j=0
                                        prev_finger_position = 0
                                        prev_finger_direction = 0
                                        for finger in hand.fingers:
                                            transformed_position = hand_transform.transform_point(finger.tip_position)
                                            transformed_direction = hand_transform.transform_direction(finger.direction)
                                            sp = finger.tip_velocity.magnitude
                                            #print finger.tip_position
                                            #print transformed_position
                                            total_speed.append(sp)
                                            name = str(self.finger_names[finger.type])

                                            #cach_dict.update({handType+"."+name+"_id" :  str(finger.id) , handType+"."+name+"_length" : str(finger.length)
                                            #                , handType+"."+name+"_width" : str(finger.width)})
                                            # TTP: tip to palm
                                            cach_dict.update({handType + "." + name + ".TTP": str(transformed_position.magnitude)})
                                            # TNA: to normal angel
                                            cach_dict.update({handType + "." + name + ".TNA": str(normal.angle_to(transformed_direction)*(180/3.14))})
                                            # print normal.angle_to(transformed_direction)*(180/3.14)

                                            if (j==0):
                                                #print name
                                                prev_name=name
                                                prev_finger_direction = finger.direction
                                                j=j+1
                                            else:
                                                #print name
                                                #print prev_finger_direction.angle_to(finger.direction)*(180/3.14)
                                                cach_dict.update({handType + "." +prev_name+"_"+ name + ".ang": str(prev_finger_direction.angle_to(finger.direction)*(180/3.14))})
                                                prev_finger_position = finger.tip_position
                                                prev_finger_direction = finger.direction
                                                prev_name=name
                                                j = j + 1







                                            # Get bones
                                            for b in range(0, 4):
                                                bone = finger.bone(b)
                                                name2=handType+"."+name+ "_" + str(self.bone_names[bone.type])
                                                #cach_dict.update({name2+ "_s_x" : str(bone.prev_joint[0]) ,name2+ "_s_y" : str(bone.prev_joint[1]) ,name2+ "_s_z" : str(bone.prev_joint[2]) ,name2 + "_e_x" : str(bone.next_joint[0]),name2 + "_e_y" : str(bone.next_joint[1]) ,name2 + "_e_z" : str(bone.next_joint[2])  ,name2 +"_d_x" : str(bone.direction[0]),name2 +"_d_y" : str(bone.direction[1]),name2 +"_d_z" : str(bone.direction[2])})


                                    if not frame.hands.is_empty:
                                        pass



                                    c=pd.DataFrame.from_dict(cach_dict.values(), orient="columns", dtype=float)

                                    c=c.transpose()

                                    #print(c)
                                    #print(c.shape)

                                    d=d.append(c,ignore_index=True )

                                    if ((max(total_speed))  <= 70):

                                        w=averaging(d)

                                        #print(w.shape)

                                        #print(w)

                                        #print(w.ix[0])
                                        w=w.ix[0]
                                        w=w.values.reshape(1,-1)
                                        #print(w.shape)

                                        prd(w)


                                        d=pd.DataFrame(dtype=float)
                                        time.sleep(1)





def averaging(inputframe):

    #for typ in type:
    #print(inputframe.shape)
    inputframe = inputframe.reset_index(drop=True)
    #print(inputframe.shape)
    #print(inputframe.shape)
    #inputframe = inputframe[[429,430,431,432,433,434,435,436,437,438,439,
    #440,441,442,443,444,445,446,447,448,449,450,
    #451,452,453,454,455,456]]


    inputframe=inputframe.groupby(np.arange(len(inputframe))//L).mean()

    return (inputframe)





def main():
            # Create a sample listener and controller
            global filename
            global ges_type,si


            #si = subprocess.STARTUPINFO()
            #si =subprocess.Popen("C:\Program Files (x86)\Leap Motion\Core Services\Visualizer.exe")

            listener = SampleListener()
            controller = Leap.Controller()

            # Have the sample listener receive events from the controller
            controller.add_listener(listener)

            # Keep this process running until Enter is pressed
            print("Press Enter to quit...  ")


            try:
                sys.stdin.readline()
            except KeyboardInterrupt:
                pass
            finally:
                # Remove the sample listener when done
                controller.remove_listener(listener)
                # csvfile.close()

if __name__ == "__main__":
            main()
