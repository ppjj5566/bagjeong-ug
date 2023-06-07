import servo_state
import leg_inverse_kinematic
from math import pi,sqrt,atan2,atan,tan,cos,sin

coxia = 14.4
fermur = 43.6
tidia = 74.2
coxferlen = 58
body_side_length = 57.5
cos_60 = 0.5
sin_60 = 0.86602

feet_position_x = cos_60 * coxferlen
feet_position_y = sin_60 * coxferlen
feet_position_z = tidia

body_center_offset_x = body_side_length / 2
body_center_offset_y = sqrt(body_side_length ** 2 - body_center_offset_x ** 2)

#[몸체 중심에서 골반까지의 x 성분거리, 몸체 중심에서 골반까지의 y 성분거리, 골반에서 발까지의 x성분거리, 골반에서 발까지의 y성분거리, 골반에서 발까지의 z성분거리]
leg_1_position = [-body_center_offset_x,  body_center_offset_y,  -feet_position_x,  feet_position_y, -feet_position_z]
leg_2_position = [-body_side_length,                         0,  -coxferlen,                       0, -feet_position_z]
leg_3_position = [-body_center_offset_x, -body_center_offset_y,  -feet_position_x,  -feet_position_y, -feet_position_z]
leg_4_position = [body_center_offset_x,   body_center_offset_y,   feet_position_x,  feet_position_y, -feet_position_z]
leg_5_position = [body_side_length,                          0,   coxferlen,                       0, -feet_position_z]
leg_6_position = [body_center_offset_x,  -body_center_offset_y,   feet_position_x,  -feet_position_y, -feet_position_z]

leg_position = [leg_1_position,leg_2_position,leg_3_position,
                leg_4_position,leg_5_position,leg_6_position] 


def inverseKinematic(x = 0, y = 0, z = 0, rot_x = 0, rot_y = 0, rot_z = 0, leg_number = 0):
    total_x = leg_position[leg_number][0] + leg_position[leg_number][2] + x
    total_y = leg_position[leg_number][1] + leg_position[leg_number][3] + y
    dist_body_center_feet = sqrt(total_x ** 2 + total_y ** 2)
    angle_body_center = atan2(total_y, total_x)
    roll_z = tan(rot_z * pi / 180) * total_x
    pitch_z = tan(rot_x * pi / 180) * total_y
    body_ikx = (cos(angle_body_center + (rot_y * pi / 180)) * dist_body_center_feet) - total_x
    body_iky = (sin(angle_body_center + (rot_y * pi / 180)) * dist_body_center_feet) - total_y
    body_ikz = roll_z + pitch_z
    leg_inverse_kinematic.leg_kinematic(x, y, z, body_ikx, body_iky, body_ikz, leg_number)
    #print("----------------------------------------------")
    #print("ik :", body_ikx, body_iky, body_ikz)

def bodyInverseKinematic(x = 0, y = 0, z = 0, rot_x = 0, rot_y = 0, rot_z = 0):
    inverseKinematic(x, y, z, rot_x, rot_y, rot_z, 0)
    inverseKinematic(x, y, z, rot_x, rot_y, rot_z, 1)
    inverseKinematic(x, y, z, rot_x, rot_y, rot_z, 2)
    inverseKinematic(x, y, z, rot_x, rot_y, rot_z, 3)
    inverseKinematic(x, y, z, rot_x, rot_y, rot_z, 4)
    inverseKinematic(x, y, z, rot_x, rot_y, rot_z, 5)