import servo_state
import body_inverse_kinematic
import body_forward_kinematic
import time


class ForwardKinematics():
    max_distance = 23
    min_distance = -23
    max_heigth = -25
    last_moved_distance = 5
    #stance_sequence = [-25,-20,-15,-10,-5,0,5,10,15,20,25]
    #swing_sequence = [0,6,10,15,20,25,20,15,10,6,0]
    last_stance_end_x = 0
    last_stance_end_y = 0
    bezier_stance_y = []
    bezier_stance_x = []
    bezier_swing = []
    sequence_length = 0
    state = 0
    
    def __init__(self):
        pass


    def bezier_stance(self, last_sequence_x, last_sequence_y, sequence, x_cos, y_sin):
        self.bezier_stance_x = []
        self.bezier_stance_y = []
        self.bezier_swing = []
        for i in range(-last_sequence_x, sequence, 2):
            self.bezier_stance_x.append(i * x_cos)
        for i in range(-last_sequence_y, sequence, 2):
            self.bezier_stance_y.append(i * y_sin)
        for z in range(0, sequence + 1, 2):
            self.bezier_swing.append(z)
        for z in range(sequence + 1, 0, -2):
            self.bezier_swing.append(z)
        self.sequence_length = len(self.bezier_stance_x)


    def bezier_swing(self, last_sequence_x, last_sequence_y, sequence, x_cos, y_sin):
        ForwardKinematics.bezier_stance_x = []
        ForwardKinematics.bezier_stance_y = []
        ForwardKinematics.bezier_swing = []
        for i in range(last_sequence_x, -sequence, 2):
            ForwardKinematics.bezier_stance_x.append(i * x_cos)
        for i in range(last_sequence_y, -sequence, 2):
            ForwardKinematics.bezier_stance_y.append(i * y_sin)
        for z in range(0, sequence + 1, 2):
            ForwardKinematics.bezier_swing.append(z)
        for z in range(sequence + 1, 0, -2):
            ForwardKinematics.bezier_swing.append(z)
        ForwardKinematics.sequence_length = len(ForwardKinematics.bezier_stance_x)
        
    # 몸체를 움직이는 것은 state = 0으로 하고 다음 다리의 위치로 옮기는 것을 State =1로 설정한다.
    # 현재의 움직임의 위치를 x, y변수에 저쟝한다.
    # 움직여야하는 벡터는 cos과 sin값의 인수를 x,y값에 대입한다.

    def propelling(self, x_cos, y_sin, moving_distance):
        max_heigth = ForwardKinematics.max_heigth
        state = ForwardKinematics.state
        last_stance_end_x = ForwardKinematics.last_stance_end_x
        last_stance_end_y = ForwardKinematics.last_stance_end_y
        if moving_distance > 40:
            self.bezier_stance(last_stance_end_x, last_stance_end_y, 25, x_cos, y_sin)
            if state == 0:
                for i in range(ForwardKinematics.sequence_length):
                    body_inverse_kinematic.inverseKinematic(x= ForwardKinematics.bezier_stance_x[i], y = ForwardKinematics.bezier_stance_y[i], z = max_heigth, leg_number = 0)
                    body_inverse_kinematic.inverseKinematic(x= -ForwardKinematics.bezier_stance_x[i], y = -ForwardKinematics.bezier_stance_y[i], z = max_heigth - ForwardKinematics.bezier_swing[i], leg_number = 1)
                    body_inverse_kinematic.inverseKinematic(x= ForwardKinematics.bezier_stance_x[i], y = ForwardKinematics.bezier_stance_y[i], z = max_heigth, leg_number = 2)
                    body_inverse_kinematic.inverseKinematic(x= ForwardKinematics.bezier_stance_x[i], y = ForwardKinematics.bezier_stance_y[i], z = max_heigth - ForwardKinematics.bezier_swing[i], leg_number = 3)
                    body_inverse_kinematic.inverseKinematic(x= ForwardKinematics.bezier_stance_x[i], y = ForwardKinematics.bezier_stance_y[i], z = max_heigth, leg_number = 4)
                    body_inverse_kinematic.inverseKinematic(x= ForwardKinematics.bezier_stance_x[i], y = ForwardKinematics.bezier_stance_y[i], z = max_heigth - ForwardKinematics.bezier_swing[i], leg_number = 5)
                    time.sleep(0.01)
                ForwardKinematics.state = 1
                ForwardKinematics.last_stance_end_x = int(ForwardKinematics.bezier_stance_x[-1])
                ForwardKinematics.last_stance_end_y = int(ForwardKinematics.bezier_stance_y[-1])

            if state == 1:
                self.bezier_swing(last_stance_end_x, last_stance_end_y, 25, x_cos, y_sin)
                for i in range(ForwardKinematics.sequence_length):
                    body_inverse_kinematic.inverseKinematic(x= -ForwardKinematics.bezier_stance_x[i], y = -ForwardKinematics.bezier_stance_y[i] * y_sin, z = max_heigth - ForwardKinematics.bezier_swing[i], leg_number = 0)
                    body_inverse_kinematic.inverseKinematic(x= ForwardKinematics.bezier_stance_x[i], y = ForwardKinematics.bezier_stance_y[i] * y_sin, z = max_heigth, leg_number = 1)
                    body_inverse_kinematic.inverseKinematic(x= -ForwardKinematics.bezier_stance_x[i], y = -ForwardKinematics.bezier_stance_y[i] * y_sin, z = max_heigth - ForwardKinematics.bezier_swing[i], leg_number = 2)
                    body_inverse_kinematic.inverseKinematic(x= -ForwardKinematics.bezier_stance_x[i], y = -ForwardKinematics.bezier_stance_y[i] * y_sin, z = max_heigth, leg_number = 3)
                    body_inverse_kinematic.inverseKinematic(x= -ForwardKinematics.bezier_stance_x[i], y = -ForwardKinematics.bezier_stance_y[i] * y_sin, z = max_heigth - ForwardKinematics.bezier_swing[i], leg_number = 4)
                    body_inverse_kinematic.inverseKinematic(x= -ForwardKinematics.bezier_stance_x[i], y = -ForwardKinematics.bezier_stance_y[i] * y_sin, z = max_heigth, leg_number = 5)
                    time.sleep(0.01)
                ForwardKinematics.state = 0
                ForwardKinematics.last_stance_end_x = int(ForwardKinematics.bezier_stance_x[-1])
                ForwardKinematics.last_stance_end_y = int(ForwardKinematics.bezier_stance_y[-1])
            else:
                pass
        else:
            pass


    def body_move(self, x_cos, y_sin, moving_distance):
        moving_distance = moving_distance / 3
        body_inverse_kinematic.inverseKinematic(x= moving_distance * x_cos, y = moving_distance * y_sin, z = -20, leg_number = 0)
        body_inverse_kinematic.inverseKinematic(x= moving_distance * x_cos, y = moving_distance * y_sin, z = -20, leg_number = 1)
        body_inverse_kinematic.inverseKinematic(x= moving_distance * x_cos, y = moving_distance * y_sin, z = -20, leg_number = 2)
        body_inverse_kinematic.inverseKinematic(x= -moving_distance * x_cos, y = -moving_distance * y_sin, z = -20, leg_number = 3)
        body_inverse_kinematic.inverseKinematic(x= moving_distance * x_cos, y = moving_distance * y_sin, z = -20, leg_number = 4)
        body_inverse_kinematic.inverseKinematic(x= -moving_distance * x_cos, y = -moving_distance * y_sin, z = -20, leg_number = 5)
