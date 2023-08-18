import kinematic.body_inverse_kinematic as body_inverse_kinematic
import time

class BodyForwardKinematic():
    distance = 40
    z_heigth = -30
    stances = []
    swings = []
    state = 0

    def __init__(self, leg_number):
        self.leg_number = leg_number

    def stance(self):
        self.stances = []
        for i in range(-self.distance, self.distance + 5, 5):
            self.stances.append(i)
        #print(self.stances, self.state)

    def swing(self):
        self.swings = []
        for i in range(0, self.distance, 5):
            self.swings.append(i)
        for i in range(self.distance, -5, -5):
            self.swings.append(i) 
        #print(self.swings, self.state)

    def leg_movement(self, x_cos, y_sin):
        if x_cos != 0 or y_sin != 0:
            self.swing()
            self.stance()
            if self.state == 0:
                self.state = 1
                for x in range(len(self.stances)):
                    body_inverse_kinematic.inverseKinematic(x = (self.stances[x] / 2) * x_cos, 
                                                            y = self.stances[x] * y_sin, 
                                                            z = self.z_heigth, 
                                                            leg_number = 0)
                    body_inverse_kinematic.inverseKinematic(x = (self.stances[x] / 2) * x_cos, 
                                                            y = self.stances[-x - 1] * y_sin, 
                                                            z = self.z_heigth - (self.swings[x] / 1.5), 
                                                            leg_number = 1)
                    body_inverse_kinematic.inverseKinematic(x = (self.stances[x] / 2) * x_cos, 
                                                            y = self.stances[x] * y_sin, 
                                                            z = self.z_heigth, 
                                                            leg_number = 2)
                    body_inverse_kinematic.inverseKinematic(x = (self.stances[x] / 2) * x_cos, 
                                                            y = self.stances[-x - 1] * y_sin, 
                                                            z = self.z_heigth - (self.swings[x] / 1.5), 
                                                            leg_number = 3)
                    body_inverse_kinematic.inverseKinematic(x = (self.stances[x] / 2) * x_cos, 
                                                            y = self.stances[x] * y_sin, 
                                                            z = self.z_heigth, 
                                                            leg_number = 4)
                    body_inverse_kinematic.inverseKinematic(x = (self.stances[x] / 2) * x_cos, 
                                                            y = self.stances[-x - 1] * y_sin, 
                                                            z = self.z_heigth -  (self.swings[x] / 1.5), 
                                                            leg_number = 5)
                    #print("-------------------------------------------------------------------")
                    time.sleep(0.010)
                

            elif self.state == 1:
                self.state = 0
                for x in range(len(self.stances)):
                    body_inverse_kinematic.inverseKinematic(x = (self.stances[x] / 2) * x_cos, 
                                                            y = self.stances[-x - 1] * y_sin, 
                                                            z = self.z_heigth -  (self.swings[x] / 1.5), 
                                                            leg_number = 0)
                    body_inverse_kinematic.inverseKinematic(x = (self.stances[x] / 2) * x_cos, 
                                                            y = self.stances[x] * y_sin, 
                                                            z = self.z_heigth, 
                                                            leg_number = 1)
                    body_inverse_kinematic.inverseKinematic(x = (self.stances[x] / 2) * x_cos, 
                                                            y = self.stances[-x - 1] * y_sin, 
                                                            z = self.z_heigth -  (self.swings[x] / 1.5), 
                                                            leg_number = 2)
                    body_inverse_kinematic.inverseKinematic(x = (self.stances[x] / 2) * x_cos, 
                                                            y = self.stances[x] * y_sin, 
                                                            z = self.z_heigth, 
                                                            leg_number = 3)
                    body_inverse_kinematic.inverseKinematic(x = (self.stances[x] / 2) * x_cos, 
                                                            y = self.stances[-x - 1] * y_sin, 
                                                            z = self.z_heigth -  (self.swings[x] / 1.5) , 
                                                            leg_number = 4)
                    body_inverse_kinematic.inverseKinematic(x = (self.stances[x] / 2) * x_cos, 
                                                            y = self.stances[x] * y_sin, 
                                                            z = self.z_heigth ,
                                                            leg_number = 5)
                    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    time.sleep(0.010)