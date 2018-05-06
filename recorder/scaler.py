################################################################################
# Copyright (C) 2012-2016 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################


'''
*change person number only for every person
*open visulaizer manually

'''




#line 34 change writeheader  in case of append to False

import Leap, sys, time, csv,os
import string
import numpy as np




class SampleListener(Leap.Listener):
            finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
            bone_names = ['M', 'P', 'I', 'D']
            state_names = ["STATE INVALID", "STATE START","STATE END","STATE UPDATE"]
            global fieldnames , writeheaders , second_iteration , start_time,count ,person , l_s , r_s
            l_s=0
            r_s=0
            person=8
            gate=True
            second_iteration = False
            writeheaders = True
            count = 0
            start_time = 0
            fieldnames = ['Frame id', 'timestamp', 'hands', 'fingers'
                    , 'L.hand', 'L.hand.id', 'L.hand.palm_position_x', 'L.hand.palm_position_y',
                              'L.hand.palm_position_z'
                    , 'L.pitch', 'L.roll', 'L.yaw', 'L.Arm direction_x', 'L.Arm direction_y', 'L.Arm direction_z'
                    , 'L.wrist position_x', 'L.wrist position_y', 'L.wrist position_z'
                    , 'L.elbow position_x', 'L.elbow position_y', 'L.elbow position_z'
                    , 'L.Thumb_id', 'L.Thumb_length', 'L.Thumb_width'
                    , 'L.Index_id', 'L.Index_length', 'L.Index_width'
                    , 'L.Middle_id', 'L.Middle_length', 'L.Middle_width'
                    , 'L.Ring_id', 'L.Ring_length', 'L.Ring_width'
                    , 'L.Pinky_id', 'L.Pinky_length', 'L.Pinky_width'
                    , 'L.Thumb_M_s_x', 'L.Thumb_M_s_y', 'L.Thumb_M_s_z', 'L.Thumb_M_e_x', 'L.Thumb_M_e_y',
                              'L.Thumb_M_e_z',
                              'L.Thumb_M_d_x', 'L.Thumb_M_d_y', 'L.Thumb_M_d_z', 'L.Thumb_P_s_x', 'L.Thumb_P_s_y',
                              'L.Thumb_P_s_z',
                              'L.Thumb_P_e_x', 'L.Thumb_P_e_y', 'L.Thumb_P_e_z', 'L.Thumb_P_d_x', 'L.Thumb_P_d_y',
                              'L.Thumb_P_d_z',
                              'L.Thumb_I_s_x', 'L.Thumb_I_s_y', 'L.Thumb_I_s_z', 'L.Thumb_I_e_x', 'L.Thumb_I_e_y',
                              'L.Thumb_I_e_z',
                              'L.Thumb_I_d_x', 'L.Thumb_I_d_y', 'L.Thumb_I_d_z', 'L.Thumb_D_s_x', 'L.Thumb_D_s_y',
                              'L.Thumb_D_s_z',
                              'L.Thumb_D_e_x', 'L.Thumb_D_e_y', 'L.Thumb_D_e_z', 'L.Thumb_D_d_x', 'L.Thumb_D_d_y',
                              'L.Thumb_D_d_z'
                    , 'L.Index_M_s_x', 'L.Index_M_s_y', 'L.Index_M_s_z', 'L.Index_M_e_x', 'L.Index_M_e_y',
                              'L.Index_M_e_z',
                              'L.Index_M_d_x', 'L.Index_M_d_y', 'L.Index_M_d_z', 'L.Index_P_s_x', 'L.Index_P_s_y',
                              'L.Index_P_s_z',
                              'L.Index_P_e_x', 'L.Index_P_e_y', 'L.Index_P_e_z', 'L.Index_P_d_x', 'L.Index_P_d_y',
                              'L.Index_P_d_z',
                              'L.Index_I_s_x', 'L.Index_I_s_y', 'L.Index_I_s_z', 'L.Index_I_e_x', 'L.Index_I_e_y',
                              'L.Index_I_e_z',
                              'L.Index_I_d_x', 'L.Index_I_d_y', 'L.Index_I_d_z', 'L.Index_D_s_x', 'L.Index_D_s_y',
                              'L.Index_D_s_z',
                              'L.Index_D_e_x', 'L.Index_D_e_y', 'L.Index_D_e_z', 'L.Index_D_d_x', 'L.Index_D_d_y',
                              'L.Index_D_d_z'
                    , 'L.Middle_M_s_x', 'L.Middle_M_s_y', 'L.Middle_M_s_z', 'L.Middle_M_e_x', 'L.Middle_M_e_y',
                              'L.Middle_M_e_z',
                              'L.Middle_M_d_x', 'L.Middle_M_d_y', 'L.Middle_M_d_z', 'L.Middle_P_s_x', 'L.Middle_P_s_y',
                              'L.Middle_P_s_z', 'L.Middle_P_e_x', 'L.Middle_P_e_y', 'L.Middle_P_e_z', 'L.Middle_P_d_x',
                              'L.Middle_P_d_y', 'L.Middle_P_d_z', 'L.Middle_I_s_x', 'L.Middle_I_s_y', 'L.Middle_I_s_z',
                              'L.Middle_I_e_x', 'L.Middle_I_e_y', 'L.Middle_I_e_z', 'L.Middle_I_d_x', 'L.Middle_I_d_y',
                              'L.Middle_I_d_z', 'L.Middle_D_s_x', 'L.Middle_D_s_y', 'L.Middle_D_s_z', 'L.Middle_D_e_x',
                              'L.Middle_D_e_y', 'L.Middle_D_e_z', 'L.Middle_D_d_x', 'L.Middle_D_d_y', 'L.Middle_D_d_z'
                    , 'L.Ring_M_s_x', 'L.Ring_M_s_y', 'L.Ring_M_s_z', 'L.Ring_M_e_x', 'L.Ring_M_e_y', 'L.Ring_M_e_z',
                              'L.Ring_M_d_x', 'L.Ring_M_d_y', 'L.Ring_M_d_z', 'L.Ring_P_s_x', 'L.Ring_P_s_y',
                              'L.Ring_P_s_z',
                              'L.Ring_P_e_x', 'L.Ring_P_e_y', 'L.Ring_P_e_z', 'L.Ring_P_d_x', 'L.Ring_P_d_y',
                              'L.Ring_P_d_z',
                              'L.Ring_I_s_x', 'L.Ring_I_s_y', 'L.Ring_I_s_z', 'L.Ring_I_e_x', 'L.Ring_I_e_y',
                              'L.Ring_I_e_z',
                              'L.Ring_I_d_x', 'L.Ring_I_d_y', 'L.Ring_I_d_z', 'L.Ring_D_s_x', 'L.Ring_D_s_y',
                              'L.Ring_D_s_z',
                              'L.Ring_D_e_x', 'L.Ring_D_e_y', 'L.Ring_D_e_z', 'L.Ring_D_d_x', 'L.Ring_D_d_y',
                              'L.Ring_D_d_z'
                    , 'L.Pinky_M_s_x', 'L.Pinky_M_s_y', 'L.Pinky_M_s_z', 'L.Pinky_M_e_x', 'L.Pinky_M_e_y',
                              'L.Pinky_M_e_z',
                              'L.Pinky_M_d_x', 'L.Pinky_M_d_y', 'L.Pinky_M_d_z', 'L.Pinky_P_s_x', 'L.Pinky_P_s_y',
                              'L.Pinky_P_s_z',
                              'L.Pinky_P_e_x', 'L.Pinky_P_e_y', 'L.Pinky_P_e_z', 'L.Pinky_P_d_x', 'L.Pinky_P_d_y',
                              'L.Pinky_P_d_z',
                              'L.Pinky_I_s_x', 'L.Pinky_I_s_y', 'L.Pinky_I_s_z', 'L.Pinky_I_e_x', 'L.Pinky_I_e_y',
                              'L.Pinky_I_e_z',
                              'L.Pinky_I_d_x', 'L.Pinky_I_d_y', 'L.Pinky_I_d_z', 'L.Pinky_D_s_x', 'L.Pinky_D_s_y',
                              'L.Pinky_D_s_z',
                              'L.Pinky_D_e_x', 'L.Pinky_D_e_y', 'L.Pinky_D_e_z', 'L.Pinky_D_d_x', 'L.Pinky_D_d_y',
                              'L.Pinky_D_d_z', 'R.hand', 'R.hand.id', 'R.hand.palm_position_x',
                              'R.hand.palm_position_y', 'R.hand.palm_position_z'
                    , 'R.pitch', 'R.roll', 'R.yaw', 'R.Arm direction_x', 'R.Arm direction_y', 'R.Arm direction_z'
                    , 'R.wrist position_x', 'R.wrist position_y', 'R.wrist position_z'
                    , 'R.elbow position_x', 'R.elbow position_y', 'R.elbow position_z'
                    , 'R.Thumb_id', 'R.Thumb_length', 'R.Thumb_width'
                    , 'R.Index_id', 'R.Index_length', 'R.Index_width'
                    , 'R.Middle_id', 'R.Middle_length', 'R.Middle_width'
                    , 'R.Ring_id', 'R.Ring_length', 'R.Ring_width'
                    , 'R.Pinky_id', 'R.Pinky_length', 'R.Pinky_width'
                    , 'R.Thumb_M_s_x', 'R.Thumb_M_s_y', 'R.Thumb_M_s_z', 'R.Thumb_M_e_x', 'R.Thumb_M_e_y',
                              'R.Thumb_M_e_z',
                              'R.Thumb_M_d_x', 'R.Thumb_M_d_y', 'R.Thumb_M_d_z', 'R.Thumb_P_s_x', 'R.Thumb_P_s_y',
                              'R.Thumb_P_s_z',
                              'R.Thumb_P_e_x', 'R.Thumb_P_e_y', 'R.Thumb_P_e_z', 'R.Thumb_P_d_x', 'R.Thumb_P_d_y',
                              'R.Thumb_P_d_z',
                              'R.Thumb_I_s_x', 'R.Thumb_I_s_y', 'R.Thumb_I_s_z', 'R.Thumb_I_e_x', 'R.Thumb_I_e_y',
                              'R.Thumb_I_e_z',
                              'R.Thumb_I_d_x', 'R.Thumb_I_d_y', 'R.Thumb_I_d_z', 'R.Thumb_D_s_x', 'R.Thumb_D_s_y',
                              'R.Thumb_D_s_z',
                              'R.Thumb_D_e_x', 'R.Thumb_D_e_y', 'R.Thumb_D_e_z', 'R.Thumb_D_d_x', 'R.Thumb_D_d_y',
                              'R.Thumb_D_d_z'
                    , 'R.Index_M_s_x', 'R.Index_M_s_y', 'R.Index_M_s_z', 'R.Index_M_e_x', 'R.Index_M_e_y',
                              'R.Index_M_e_z',
                              'R.Index_M_d_x', 'R.Index_M_d_y', 'R.Index_M_d_z', 'R.Index_P_s_x', 'R.Index_P_s_y',
                              'R.Index_P_s_z',
                              'R.Index_P_e_x', 'R.Index_P_e_y', 'R.Index_P_e_z', 'R.Index_P_d_x', 'R.Index_P_d_y',
                              'R.Index_P_d_z',
                              'R.Index_I_s_x', 'R.Index_I_s_y', 'R.Index_I_s_z', 'R.Index_I_e_x', 'R.Index_I_e_y',
                              'R.Index_I_e_z',
                              'R.Index_I_d_x', 'R.Index_I_d_y', 'R.Index_I_d_z', 'R.Index_D_s_x', 'R.Index_D_s_y',
                              'R.Index_D_s_z',
                              'R.Index_D_e_x', 'R.Index_D_e_y', 'R.Index_D_e_z', 'R.Index_D_d_x', 'R.Index_D_d_y',
                              'R.Index_D_d_z'
                    , 'R.Middle_M_s_x', 'R.Middle_M_s_y', 'R.Middle_M_s_z', 'R.Middle_M_e_x', 'R.Middle_M_e_y',
                              'R.Middle_M_e_z',
                              'R.Middle_M_d_x', 'R.Middle_M_d_y', 'R.Middle_M_d_z', 'R.Middle_P_s_x', 'R.Middle_P_s_y',
                              'R.Middle_P_s_z', 'R.Middle_P_e_x', 'R.Middle_P_e_y', 'R.Middle_P_e_z', 'R.Middle_P_d_x',
                              'R.Middle_P_d_y', 'R.Middle_P_d_z', 'R.Middle_I_s_x', 'R.Middle_I_s_y', 'R.Middle_I_s_z',
                              'R.Middle_I_e_x', 'R.Middle_I_e_y', 'R.Middle_I_e_z', 'R.Middle_I_d_x', 'R.Middle_I_d_y',
                              'R.Middle_I_d_z', 'R.Middle_D_s_x', 'R.Middle_D_s_y', 'R.Middle_D_s_z', 'R.Middle_D_e_x',
                              'R.Middle_D_e_y', 'R.Middle_D_e_z', 'R.Middle_D_d_x', 'R.Middle_D_d_y', 'R.Middle_D_d_z'
                    , 'R.Ring_M_s_x', 'R.Ring_M_s_y', 'R.Ring_M_s_z', 'R.Ring_M_e_x', 'R.Ring_M_e_y', 'R.Ring_M_e_z',
                              'R.Ring_M_d_x', 'R.Ring_M_d_y', 'R.Ring_M_d_z', 'R.Ring_P_s_x', 'R.Ring_P_s_y',
                              'R.Ring_P_s_z',
                              'R.Ring_P_e_x', 'R.Ring_P_e_y', 'R.Ring_P_e_z', 'R.Ring_P_d_x', 'R.Ring_P_d_y',
                              'R.Ring_P_d_z',
                              'R.Ring_I_s_x', 'R.Ring_I_s_y', 'R.Ring_I_s_z', 'R.Ring_I_e_x', 'R.Ring_I_e_y',
                              'R.Ring_I_e_z',
                              'R.Ring_I_d_x', 'R.Ring_I_d_y', 'R.Ring_I_d_z', 'R.Ring_D_s_x', 'R.Ring_D_s_y',
                              'R.Ring_D_s_z',
                              'R.Ring_D_e_x', 'R.Ring_D_e_y', 'R.Ring_D_e_z', 'R.Ring_D_d_x', 'R.Ring_D_d_y',
                              'R.Ring_D_d_z'
                    , 'R.Pinky_M_s_x', 'R.Pinky_M_s_y', 'R.Pinky_M_s_z', 'R.Pinky_M_e_x', 'R.Pinky_M_e_y',
                              'R.Pinky_M_e_z',
                              'R.Pinky_M_d_x', 'R.Pinky_M_d_y', 'R.Pinky_M_d_z', 'R.Pinky_P_s_x', 'R.Pinky_P_s_y',
                              'R.Pinky_P_s_z',
                              'R.Pinky_P_e_x', 'R.Pinky_P_e_y', 'R.Pinky_P_e_z', 'R.Pinky_P_d_x', 'R.Pinky_P_d_y',
                              'R.Pinky_P_d_z',
                              'R.Pinky_I_s_x', 'R.Pinky_I_s_y', 'R.Pinky_I_s_z', 'R.Pinky_I_e_x', 'R.Pinky_I_e_y',
                              'R.Pinky_I_e_z',
                              'R.Pinky_I_d_x', 'R.Pinky_I_d_y', 'R.Pinky_I_d_z', 'R.Pinky_D_s_x', 'R.Pinky_D_s_y',
                              'R.Pinky_D_s_z',
                              'R.Pinky_D_e_x', 'R.Pinky_D_e_y', 'R.Pinky_D_e_z', 'R.Pinky_D_d_x', 'R.Pinky_D_d_y',
                              'R.Pinky_D_d_z',
                          'R.Thumb.TTP','R.Index.TTP','R.Middle.TTP','R.Ring.TTP','R.Pinky.TTP','L.Thumb.TTP',
                          'L.Index.TTP','L.Middle.TTP','L.Ring.TTP','L.Pinky.TTP',
                          'R.Thumb.TNA', 'R.Index.TNA', 'R.Middle.TNA', 'R.Ring.TNA', 'R.Pinky.TNA', 'L.Thumb.TNA',
                          'L.Index.TNA', 'L.Middle.TNA', 'L.Ring.TNA', 'L.Pinky.TNA',
                          'R.Thumb_Index.ang', 'R.Index_Middle.ang', 'R.Middle_Ring.ang', 'R.Ring_Pinky.ang',
                          'L.Thumb_Index.ang', 'L.Index_Middle.ang', 'L.Middle_Ring.ang', 'L.Ring_Pinky.ang',
                          'R.sphere_center_x','R.sphere_center_y','R.sphere_center_z',
                          'L.sphere_center_x','L.sphere_center_y','L.sphere_center_z',
                          'R_scaling_factor','L_scaling_factor','R.Thumb.TTP_sacled','R.Index.TTP_sacled','R.Middle.TTP_sacled','R.Ring.TTP_sacled','R.Pinky.TTP_sacled',
                          'L.Thumb.TTP_sacled','L.Index.TTP_sacled','L.Middle.TTP_sacled','L.Ring.TTP_sacled','L.Pinky.TTP_sacled'

                          ]


                # run only once per file then make it comment


            def on_init(self, controller):
                     print(" Initialized ")

            def on_connect(self, controller):
                     print(" Connected ")


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
                        global count,gate,person, l_s , r_s



                        frame = controller.frame()
                        #for gesture in frame.gestures():
                        gesture=frame.gestures()

                        if(second_iteration==False):
                                        print("START recording AFTER:")
                                        for x in range(1,4,1):
                                            print(x)
                                            time.sleep(1)
                                            if(x==3):
                                                print ("RECORDING")
                                        second_iteration = True

                        if (len(frame.hands) <= 2) and (len(frame.hands)!= 0):
                                        total_speed = []



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

                                            #cach_dict.update({handType+".hand": 1,handType+".hand.id": str(hand.id) ,handType+".hand.palm_position_x": str(hand.palm_position[0]),handType+".hand.palm_position_y": str(hand.palm_position[1]),handType+".hand.palm_position_z": str(hand.palm_position[2])})
                                            #print hand.palm_position

                                            # Get the hand's normal vector and direction
                                            normal = hand.palm_normal
                                            #print normal
                                            direction = hand.direction
                                            # Calculate the hand's pitch, roll, and yaw angles
                                            #cach_dict.update({handType+".pitch" : str(direction.pitch * Leap.RAD_TO_DEG) , handType+".roll" : str(normal.roll*Leap.RAD_TO_DEG) , handType+".yaw" : str(direction.yaw * Leap.RAD_TO_DEG)})


                                            # Get arm bone
                                            arm = hand.arm
                                            sphere=hand.sphere_center

                                            f=hand.fingers[2]
                                            scaling_factor=hand_transform.transform_point(f.tip_position)
                                            s=scaling_factor.magnitude

                                            if (handType=="R"):
                                                r_s=r_s + s

                                            if (handType=="L"):
                                                l_s=l_s + s




                                        if (count == 100):


                                                   print(l_s/100)
                                                   print(r_s/100)
                                                   z=np.array(((r_s/100),(l_s/100)))
                                                   print(z)

                                                   org_path= os.getcwd()
                                                   req_path=org_path+"\\dataset\\original\\static\\p" + str(person) + "\\"

                                                   if not os.path.exists(req_path):
                                                          os.makedirs(req_path)
                                                          os.chdir(req_path)
                                                   np.save(filename +'.npy', z)
                                                   req_path=org_path+"\\dataset\\original\\dynamic\\p" + str(person) + "\\"
                                                   if not os.path.exists(req_path):
                                                          os.makedirs(req_path)
                                                          os.chdir(req_path)
                                                   np.save(filename +'.npy', z)
                                                   os.chdir(org_path)
                                                   sys.exit("REOCRDING FINSHED")

                                        count=count+1

                                        if not frame.hands.is_empty:
                                            pass






def main():
            # Create a sample listener and controller
            global filename
            global ges_type
            filename="factor"
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
