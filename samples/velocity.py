


import Leap, sys, thread, time, csv


import numpy


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['M', 'P', 'I', 'D']
    state_names = ["STATE INVALID", "STATE START", "STATE END", "STATE UPDATE"]

    def on_init(self, controller):
        print(" Initialized ")

    def on_connect(self, controller):
        print(" Connected ")
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)

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

        frame = controller.frame()
        #print(frame.id)
        if (len(frame.hands) <= 2) and (len(frame.hands) != 0):
            total_speed=0
            for hand in frame.hands:
                        # 0 for right hand and 1 for left
                        velocity = hand.palm_velocity
                        #print(type(velocity))
                        #print("palm")
                        #print(velocity)
                        v2=velocity.magnitude

                        #print(v2)
                        # Get fingers
                        one_hand_speed=0
                        for finger in hand.fingers:
                            sp=finger.tip_velocity.magnitude
                        #    print("fingers")
                          #  print(sp)
                            one_hand_speed +=sp
                        total_speed += one_hand_speed
            print(total_speed/len(frame.hands))
        if not frame.hands.is_empty:
            pass
        #time.sleep(1)


def main():
    # Create a sample listener and controller
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


