import body_inverse_kinematic
import time

class BodyForwardKinematic():
    distance = 25
    state = 0
    stances = []
    swings = []
    z_heigth = -25
    length = 0

    def __init__(self, leg_number):
        self.leg_number = leg_number

    def stance(self):
        BodyForwardKinematic.stances = []
        for i in range(-BodyForwardKinematic.distance, BodyForwardKinematic.distance, 5):
            BodyForwardKinematic.stances.append(i)
        print(BodyForwardKinematic.stances, BodyForwardKinematic.state)

    def swing(self):
        BodyForwardKinematic.swings = []
        for i in range(0, BodyForwardKinematic.distance, 5):
            BodyForwardKinematic.swings.append(i) 
        for i in range(BodyForwardKinematic.distance, 0, -5):
            BodyForwardKinematic.swings.append(i) 
        print(BodyForwardKinematic.swings, BodyForwardKinematic.state)

    def leg_movement(self, x_cos, y_sin):
        if x_cos != 0 or y_sin != 0:
            self.swing()
            self.stance()
            if BodyForwardKinematic.state == 0:
                for x in range(len(BodyForwardKinematic.stances)):
                    body_inverse_kinematic.inverseKinematic(x = BodyForwardKinematic.stances[x] * x_cos, 
                                                            y = BodyForwardKinematic.stances[x] * y_sin, 
                                                            z = BodyForwardKinematic.z_heigth, 
                                                            leg_number = 0)
                    body_inverse_kinematic.inverseKinematic(x = BodyForwardKinematic.stances[-x - 1] * x_cos, 
                                                            y = BodyForwardKinematic.stances[-x - 1] * y_sin, 
                                                            z = BodyForwardKinematic.z_heigth - BodyForwardKinematic.swings[x], 
                                                            leg_number = 1)
                    body_inverse_kinematic.inverseKinematic(x = BodyForwardKinematic.stances[x] * x_cos, 
                                                            y = BodyForwardKinematic.stances[x] * y_sin, 
                                                            z = BodyForwardKinematic.z_heigth, 
                                                            leg_number = 2)
                    body_inverse_kinematic.inverseKinematic(x = BodyForwardKinematic.stances[-x - 1] * x_cos, 
                                                            y = BodyForwardKinematic.stances[-x - 1] * y_sin, 
                                                            z = BodyForwardKinematic.z_heigth - BodyForwardKinematic.swings[x], 
                                                            leg_number = 3)
                    body_inverse_kinematic.inverseKinematic(x = BodyForwardKinematic.stances[x] * x_cos, 
                                                            y = BodyForwardKinematic.stances[x] * y_sin, 
                                                            z = BodyForwardKinematic.z_heigth, 
                                                            leg_number = 4)
                    body_inverse_kinematic.inverseKinematic(x = BodyForwardKinematic.stances[-x - 1] * x_cos, 
                                                            y = BodyForwardKinematic.stances[-x - 1] * y_sin, 
                                                            z = BodyForwardKinematic.z_heigth - BodyForwardKinematic.swings[x], 
                                                            leg_number = 5)
                    time.sleep(0.003)
                BodyForwardKinematic.state = 1

            elif BodyForwardKinematic.state == 1:
                for x in range(len(BodyForwardKinematic.stances)):
                    body_inverse_kinematic.inverseKinematic(x = BodyForwardKinematic.stances[-x - 1] * x_cos, 
                                                            y = BodyForwardKinematic.stances[-x - 1] * y_sin, 
                                                            z = BodyForwardKinematic.z_heigth - BodyForwardKinematic.swings[x], 
                                                            leg_number = 0)
                    body_inverse_kinematic.inverseKinematic(x = BodyForwardKinematic.stances[x] * x_cos, 
                                                            y = BodyForwardKinematic.stances[x] * y_sin, 
                                                            z = BodyForwardKinematic.z_heigth, 
                                                            leg_number = 1)
                    body_inverse_kinematic.inverseKinematic(x = BodyForwardKinematic.stances[-x - 1] * x_cos, 
                                                            y = BodyForwardKinematic.stances[-x - 1] * y_sin, 
                                                            z = BodyForwardKinematic.z_heigth - BodyForwardKinematic.swings[x], 
                                                            leg_number = 2)
                    body_inverse_kinematic.inverseKinematic(x = BodyForwardKinematic.stances[x] * x_cos, 
                                                            y = BodyForwardKinematic.stances[x] * y_sin, 
                                                            z = BodyForwardKinematic.z_heigth, 
                                                            leg_number = 3)
                    body_inverse_kinematic.inverseKinematic(x = BodyForwardKinematic.stances[-x - 1] * x_cos, 
                                                            y = BodyForwardKinematic.stances[-x - 1] * y_sin, 
                                                            z = BodyForwardKinematic.z_heigth - BodyForwardKinematic.swings[x] , 
                                                            leg_number = 4)
                    body_inverse_kinematic.inverseKinematic(x = BodyForwardKinematic.stances[x] * x_cos, 
                                                            y = BodyForwardKinematic.stances[x] * y_sin, 
                                                            z = BodyForwardKinematic.z_heigth, 
                                                            leg_number = 5)
                    time.sleep(0.001)
                BodyForwardKinematic.state = 0