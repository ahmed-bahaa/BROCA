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

import Leap, sys, thread, time, csv,os
import string
import subprocess
#from Leap import ScreenTapGesture
import numpy as np




class SampleListener(Leap.Listener):
            finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
            bone_names = ['M', 'P', 'I', 'D']
            state_names = ["STATE INVALID", "STATE START","STATE END","STATE UPDATE"]
            global fieldnames , writeheaders , second_iteration , start_time , elapsed , ges_type , si , gate ,person,s_l,s_r
            person=1
            gate=True
            second_iteration = False
            writeheaders = True
            elapsed = 0
            start_time = 0
            s_r,s_l=np.load("C://Users//vegon//Desktop//BROCA//BROCA//recorder//dataset//original//static//p" + str(person) + "//factor.npy")
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
                             , 'R.Thumb_tip_x', 'R.Thumb_tip_y', 'R.Thumb_tip_z'
                             , 'R.Index_tip_x', 'R.Index_tip_y', 'R.Index_tip_z'
                             , 'R.Middle_tip_x', 'R.Middle_tip_y', 'R.Middle_tip_z'
                             , 'R.Ring_tip_x', 'R.Ring_tip_y', 'R.Ring_tip_z'
                             , 'R.Pinky_tip_x', 'R.Pinky_tip_y', 'R.Pinky_tip_z'
                              ,'L.Thumb_tip_x', 'L.Thumb_tip_y', 'L.Thumb_tip_z'
                              , 'L.Index_tip_x', 'L.Index_tip_y', 'L.Index_tip_z'
                              , 'L.Middle_tip_x', 'L.Middle_tip_y', 'L.Middle_tip_z'
                              , 'L.Ring_tip_x', 'L.Ring_tip_y', 'L.Ring_tip_z'
                              , 'L.Pinky_tip_x', 'L.Pinky_tip_y', 'L.Pinky_tip_z'

                                , 'R.Thumb_tip_scaled_x', 'R.Thumb_tip_scaled_y', 'R.Thumb_tip_scaled_z'
                                , 'R.Index_tip_scaled_x', 'R.Index_tip_scaled_y', 'R.Index_tip_scaled_z'
                                , 'R.Middle_tip_scaled_x', 'R.Middle_tip_scaled_y', 'R.Middle_tip_scaled_z'
                                , 'R.Ring_tip_scaled_x', 'R.Ring_tip_scaled_y', 'R.Ring_tip_scaled_z'
                                , 'R.Pinky_tip_scaled_x', 'R.Pinky_tip_scaled_y', 'R.Pinky_tip_scaled_z'
                                 ,'L.Thumb_tip_scaled_x', 'L.Thumb_tip_scaled_y', 'L.Thumb_tip_scaled_z'
                                 , 'L.Index_tip_scaled_x', 'L.Index_tip_scaled_y', 'L.Index_tip_scaled_z'
                                 , 'L.Middle_tip_scaled_x', 'L.Middle_tip_scaled_y', 'L.Middle_tip_scaled_z'
                                 , 'L.Ring_tip_scaled_x', 'L.Ring_tip_scaled_y', 'L.Ring_tip_scaled_z'
                                 , 'L.Pinky_tip_scaled_x', 'L.Pinky_tip_scaled_y', 'L.Pinky_tip_scaled_z'

                                , 'R.Thumb_tip_w_x',  'R.Thumb_tip_w_y', 'R.Thumb_tip_w_z'
                                , 'R.Index_tip_w_x', 'R.Index_tip_w_y', 'R.Index_tip_w_z'
                                , 'R.Middle_tip_w_x', 'R.Middle_tip_w_y','R.Middle_tip_w_z'
                                , 'R.Ring_tip_w_x',   'R.Ring_tip_w_y',  'R.Ring_tip_w_z'
                                , 'R.Pinky_tip_w_x',  'R.Pinky_tip_w_y', 'R.Pinky_tip_w_z'
                                 ,'L.Thumb_tip_w_x',   'L.Thumb_tip_w_y', 'L.Thumb_tip_w_z'
                                 , 'L.Index_tip_w_x', 'L.Index_tip_w_y', 'L.Index_tip_w_z'
                                 , 'L.Middle_tip_w_x','L.Middle_tip_w_y','L.Middle_tip_w_z'
                                 , 'L.Ring_tip_w_x',  'L.Ring_tip_w_y',  'L.Ring_tip_w_z'
                                 , 'L.Pinky_tip_w_x', 'L.Pinky_tip_w_y', 'L.Pinky_tip_w_z',
                                 "L.hand direction_x","L.hand direction_y","L.hand direction_z",
                                 "R.hand direction_x","R.hand direction_y","R.hand direction_z",
                                 "L.normal direction_x","L.normal direction_y","L.normal direction_z",
                                 "R.normal direction_x","R.normal direction_y","R.normal direction_z",
                                'R.Thumb.THA', 'R.Index.THA', 'R.Middle.THA', 'R.Ring.THA', 'R.Pinky.THA', 'L.Thumb.THA',
                                'L.Index.THA', 'L.Middle.THA', 'L.Ring.THA', 'L.Pinky.THA',

                                 'R.Thumb.transformed_direction_x', 'R.Thumb.transformed_direction_y', 'R.Thumb.transformed_direction_z'
                                , 'R.Index.transformed_direction_x', 'R.Index.transformed_direction_y', 'R.Index.transformed_direction_z'
                                , 'R.Middle.transformed_direction_x', 'R.Middle.transformed_direction_y', 'R.Middle.transformed_direction_z'
                                , 'R.Ring.transformed_direction_x', 'R.Ring.transformed_direction_y', 'R.Ring.transformed_direction_z'
                                , 'R.Pinky.transformed_direction_x', 'R.Pinky.transformed_direction_y', 'R.Pinky.transformed_direction_z'
                                 ,'L.Thumb.transformed_direction_x', 'L.Thumb.transformed_direction_y', 'L.Thumb.transformed_direction_z'
                                 , 'L.Index.transformed_direction_x', 'L.Index.transformed_direction_y', 'L.Index.transformed_direction_z'
                                 , 'L.Middle.transformed_direction_x', 'L.Middle.transformed_direction_y', 'L.Middle.transformed_direction_z'
                                 , 'L.Ring.transformed_direction_x', 'L.Ring.transformed_direction_y', 'L.Ring.transformed_direction_z'
                                 , 'L.Pinky.transformed_direction_x', 'L.Pinky.transformed_direction_y', 'L.Pinky.transformed_direction_z'

                                , 'R.Thumb.direction_x',   'R.Thumb.direction_y',  'R.Thumb.direction_z'
                                , 'R.Index.direction_x',   'R.Index.direction_y',  'R.Index.direction_z'
                                , 'R.Middle.direction_x',  'R.Middle.direction_y', 'R.Middle.direction_z'
                                , 'R.Ring.direction_x',    'R.Ring.direction_y',   'R.Ring.direction_z'
                                , 'R.Pinky.direction_x',   'R.Pinky.direction_y',  'R.Pinky.direction_z'
                                 ,'L.Thumb.direction_x',   'L.Thumb.direction_y',  'L.Thumb.direction_z'
                                 , 'L.Index.direction_x',  'L.Index.direction_y',  'L.Index.direction_z'
                                 , 'L.Middle.direction_x', 'L.Middle.direction_y', 'L.Middle.direction_z'
                                 , 'L.Ring.direction_x',   'L.Ring.direction_y',   'L.Ring.direction_z'
                                 , 'L.Pinky.direction_x',   'L.Pinky.direction_y',  'L.Pinky.direction_z'

                          ]


                # run only once per file then make it comment


            def on_init(self, controller):
                     print(" Initialized ")

            def on_connect(self, controller):
                     print(" Connected ")
                     controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
                     #controller.config.set("Gesture.ScreenTap.HistorySeconds", .1)
                     #controller.config.set("Gesture.ScreenTap.MinDistance", 1.0)
                     #controller.config.set("Gesture.ScreenTap.MinForwardVelocity", 50.0)
                     #controller.config.save()

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
                    global elapsed,gate,person,s_r,s_l

                    path="C://Users//vegon//Desktop//BROCA//BROCA//recorder//dataset//original//"+ ges_type + "//p" + str(person) + "//"
                    if not os.path.exists(path):
                                    os.makedirs(path)
                                    os.chdir(path)
                    with open(path + filename + ".csv", 'ab')as csvfile:
                        cach_dict = {key: 0 for key in fieldnames}
                        w = csv.DictWriter(csvfile, fieldnames=fieldnames)

                        if writeheaders==True:
                            w.writeheader()
                            writeheaders=False

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

                                        # previous = controller.frame(1)
                                        cach_dict.update({"Frame id" : str(frame.id) , "timestamp" : str(frame.timestamp) , "hands" : str(len(frame.hands)) ,
                                                          "fingers" : str(len(frame.fingers))})
                                        #print(cach_dict["Frame id"])




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

                                            cach_dict.update({handType+".hand": 1,handType+".hand.id": str(hand.id) ,handType+".hand.palm_position_x": str(hand.palm_position[0]),handType+".hand.palm_position_y": str(hand.palm_position[1]),handType+".hand.palm_position_z": str(hand.palm_position[2])})
                                            #print hand.palm_position


                                            # Get the hand's normal vector and direction
                                            normal = hand.palm_normal
                                            cach_dict.update({handType+".normal direction_x" : str(normal[0]) , handType+".normal direction_y" : str(normal[1])
                                            ,handType+".normal direction_z" : str(normal[2]) })
                                            #print normal
                                            direction = hand.direction
                                            cach_dict.update({handType+".hand direction_x" : str(direction[0]) , handType+".hand direction_y" : str(direction[1])
                                            ,handType+".hand direction_z" : str(direction[2]) })

                                            # Calculate the hand's pitch, roll, and yaw angles
                                            cach_dict.update({handType+".pitch" : str(direction.pitch * Leap.RAD_TO_DEG) , handType+".roll" : str(normal.roll*Leap.RAD_TO_DEG) , handType+".yaw" : str(direction.yaw * Leap.RAD_TO_DEG)})


                                        # Get arm bone
                                            arm = hand.arm
                                            cach_dict.update({handType+".Arm direction_x" : str(arm.direction[0]) ,  handType+".wrist position_x" : str(arm.wrist_position[0]) , handType+".elbow position_x" : str(arm.elbow_position[0]),
                                                        handType+".Arm direction_y" : str(arm.direction[1]) ,  handType+".wrist position_y" : str(arm.wrist_position[1]) , handType+".elbow position_y" : str(arm.elbow_position[1]),
                                                        handType+".Arm direction_z" : str(arm.direction[2]) ,  handType+".wrist position_z" : str(arm.wrist_position[2]) , handType+".elbow position_z" : str(arm.elbow_position[2]),
                                                                                 })
                                            sphere=hand.sphere_center


                                            cach_dict.update({handType + ".sphere_center_x": str(sphere[0]),
                                                              handType + ".sphere_center_y": str(sphere[1]),
                                                              handType + ".sphere_center_z": str(sphere[2])})


                                            cach_dict.update({ 'R_scaling_factor': str(s_r),'L_scaling_factor': str(s_l) })

                                            # Get fingers
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

                                                cach_dict.update({handType+"."+name+"_id" :  str(finger.id) , handType+"."+name+"_length" : str(finger.length)
                                                                , handType+"."+name+"_width" : str(finger.width)})
                                                #without transformation
                                                cach_dict.update({handType+"."+name+"_tip_w_x" : str(finger.tip_position[0]) ,  handType+"."+name+"_tip_w_y" : str(finger.tip_position[1]) ,
                                                 handType+"."+name+"_tip_w_z" : str(finger.tip_position[2]) })

                                                cach_dict.update({handType+"."+name+"_tip_x" : str(transformed_position[0]) ,  handType+"."+name+"_tip_y" : str(transformed_position[1]) ,
                                                 handType+"."+name+"_tip_z" : str(transformed_position[2]) })

                                                 #scaling x ,y and z with range -1:1
                                                if(handType=="R"):
                                                 cach_dict.update({handType+"."+name+"_tip_scaled_x" : str(transformed_position[0]/s_r) ,  handType+"."+name+"_tip_scaled_y" : str(transformed_position[1]/s_r) ,
                                                  handType+"."+name+"_tip_scaled_z" : str(transformed_position[2]/s_r) })
                                                else:
                                                 cach_dict.update({handType+"."+name+"_tip_scaled_x" : str(transformed_position[0]/s_l) ,  handType+"."+name+"_tip_scaled_y" : str(transformed_position[1]/s_l) ,
                                                  handType+"."+name+"_tip_scaled_z" : str(transformed_position[2]/s_l) })

                                                # TTP: tip to palm
                                                cach_dict.update({handType + "." + name + ".TTP": str(transformed_position.magnitude)})
                                                if(handType=="R"):
                                                    cach_dict.update({handType + "." + name + ".TTP_sacled": str(transformed_position.magnitude/s_r)})
                                                else:
                                                    cach_dict.update({handType + "." + name + ".TTP_sacled": str(transformed_position.magnitude/s_l)})
                                                # TNA: to normal angel
                                                cach_dict.update({handType + "." + name + ".TNA": str(normal.angle_to(transformed_direction)*(180/3.14))})
                                                # print normal.angle_to(transformed_direction)*(180/3.14)
                                                #THA: tip to hand angel
                                                cach_dict.update({handType + "." + name + ".THA": str(direction.angle_to(transformed_direction)*(180/3.14))})

                                                cach_dict.update({handType + "." + name + ".transformed_direction_x": str(transformed_direction[0]),
                                                                    handType + "." + name + ".transformed_direction_y": str(transformed_direction[1]),
                                                                    handType + "." + name + ".transformed_direction_z": str(transformed_direction[2])})

                                                cach_dict.update({handType + "." + name + ".direction_x": str(finger.direction[0]),
                                                                    handType + "." + name + ".direction_y": str(finger.direction[1]),
                                                                    handType + "." + name + ".direction_z": str(finger.direction[2])})

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



                                                #R.name_tip "tuple for test"  -+   R.name_tip  L.name_tip`````R.name_tip: transformed_position

                                                '''
                                                print"noraml",normal
                                                print"position",name,transformed_position

                                                #other solutions for normal to tip angels
                                                print normal.angle_to(transformed_position)*(180/3.14)
                                                print normal.angle_to(finger.tip_position) * (180 / 3.14)
                                                print normal.angle_to(finger.direction) * (180 / 3.14)

                                                #other solution angel between fingers
                                                prev_finger_position=finger.tip_position
                                                print prev_finger_position.angle_to(finger.tip_position)*(180/3.14)

                                                '''
                                                #print transformed_position.magnitude
                                                #print  hand_origin.distance_to(finger.tip_position)     right function also


                                                # Get bones
                                                for b in range(0, 4):
                                                    bone = finger.bone(b)
                                                    name2=handType+"."+name+ "_" + str(self.bone_names[bone.type])
                                                    cach_dict.update({name2+ "_s_x" : str(bone.prev_joint[0]) ,name2+ "_s_y" : str(bone.prev_joint[1]) ,name2+ "_s_z" : str(bone.prev_joint[2]) ,name2 + "_e_x" : str(bone.next_joint[0]),name2 + "_e_y" : str(bone.next_joint[1]) ,
                                                    name2 + "_e_z" : str(bone.next_joint[2])  ,name2 +"_d_x" : str(bone.direction[0]),name2 +"_d_y" : str(bone.direction[1]),name2 +"_d_z" : str(bone.direction[2])})


                                        if not frame.hands.is_empty:
                                            pass

                                        w.writerow(cach_dict)                               #changed

                                        if ((max(total_speed)) <= 150):
                                            if (gate):
                                                w.writerow({})
                                            gate=False

                                        if ((max(total_speed))  <= 70):

                                            if(start_time==0):
                                                start_time = time.time()
                                                #print(start_time)

                                            elapsed=time.time()-start_time
                                            print("time:",elapsed)
                                            if (elapsed >= .5):

                                                sys.exit("REOCRDING FINSHED")

                                        if ((max(total_speed))  >= 70):
                                            start_time=0
                                            gate=True


                                    # if((total_speed / len(frame.hands))<=70):

                                     #       sys.exit("REOCRDING FINSHED")


                    csvfile.close()




def main():
            # Create a sample listener and controller
            global filename
            global ges_type
            filename=raw_input("enter file name: ")
            ges_type=raw_input("static or dynamic gesture 's' or 'd' :")
            if (ges_type.lower()=="s"):
                ges_type='static'
            else:
                ges_type='dynamic'

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
