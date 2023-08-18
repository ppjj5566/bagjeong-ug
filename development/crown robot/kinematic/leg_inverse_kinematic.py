import math 
import servo_state as sms
import kinematic.body_inverse_kinematic as body_inverse_kinematic

def leg_kinematic(x = 0, y = 0, z = 0, body_ikx = 0, body_iky = 0, body_ikz = 0, leg = 0):
    #서보모터 축과 축사이의 거리
    coxia = 14.8
    fermur = 43.5
    tidia = 77.3

    position_x = round(body_inverse_kinematic.leg_position[leg][2] - x + body_ikx, 1)
    position_y = round(body_inverse_kinematic.leg_position[leg][3] - y + body_iky, 1)
    position_z = round(body_inverse_kinematic.leg_position[leg][4] - z + body_ikz, 1) 

    a_2 = math.sqrt((position_x ** 2) + (position_y ** 2)) - coxia
    a_3 = math.sqrt((a_2 ** 2) + (position_z ** 2))

    theta_1 = round(math.atan(position_y / position_x) * (180 / math.pi), 0)
    theta_2 = round((math.atan(position_z / a_2) + math.acos((fermur ** 2 + a_3 ** 2 - tidia ** 2) / (2 * fermur * a_3))) * (180 / math.pi), 0)
    theta_3 = round((math.acos((fermur ** 2 + tidia ** 2 - a_3 ** 2 ) / (2 * fermur * tidia)) * 180 / math.pi), 0)
    #print(f"positions: {leg}, {position_x}, {position_y}, {position_z}")
    #print(f"leg_degrees: {theta_1}, {theta_2}, {theta_3}")


    if leg == 0:
        sms.leg_offset[leg][0].position(index = sms.pca_pin_number[leg][0], degrees = sms.leg_offset_angle[leg][0] - theta_1 - 60)
        sms.leg_offset[leg][1].position(index = sms.pca_pin_number[leg][1], degrees = sms.leg_offset_angle[leg][1] + theta_2)
        sms.leg_offset[leg][2].position(index = sms.pca_pin_number[leg][2], degrees = sms.leg_offset_angle[leg][2] + theta_3 - 90)
    elif leg == 1:  
        sms.leg_offset[leg][0].position(index = sms.pca_pin_number[leg][0], degrees = sms.leg_offset_angle[leg][0] - theta_1)
        sms.leg_offset[leg][1].position(index = sms.pca_pin_number[leg][1], degrees = sms.leg_offset_angle[leg][1] + theta_2)
        sms.leg_offset[leg][2].position(index = sms.pca_pin_number[leg][2], degrees = sms.leg_offset_angle[leg][2] + theta_3 - 90)
    elif leg == 2:  
        sms.leg_offset[leg][0].position(index = sms.pca_pin_number[leg][0], degrees = sms.leg_offset_angle[leg][0] - theta_1 + 60)
        sms.leg_offset[leg][1].position(index = sms.pca_pin_number[leg][1], degrees = sms.leg_offset_angle[leg][1] + theta_2)
        sms.leg_offset[leg][2].position(index = sms.pca_pin_number[leg][2], degrees = sms.leg_offset_angle[leg][2] + theta_3 - 90)
    elif leg == 3:  
        sms.leg_offset[leg][0].position(index = sms.pca_pin_number[leg][0], degrees = sms.leg_offset_angle[leg][0] - theta_1 + 60)
        sms.leg_offset[leg][1].position(index = sms.pca_pin_number[leg][1], degrees = sms.leg_offset_angle[leg][1] + theta_2)
        sms.leg_offset[leg][2].position(index = sms.pca_pin_number[leg][2], degrees = sms.leg_offset_angle[leg][2] + theta_3 - 90)
    elif leg == 4:  
        sms.leg_offset[leg][0].position(index = sms.pca_pin_number[leg][0], degrees = sms.leg_offset_angle[leg][0] - theta_1)
        sms.leg_offset[leg][1].position(index = sms.pca_pin_number[leg][1], degrees = sms.leg_offset_angle[leg][1] + theta_2)
        sms.leg_offset[leg][2].position(index = sms.pca_pin_number[leg][2], degrees = sms.leg_offset_angle[leg][2] + theta_3 - 90)
    elif leg == 5:  
        sms.leg_offset[leg][0].position(index = sms.pca_pin_number[leg][0], degrees = sms.leg_offset_angle[leg][0] - theta_1 - 60)
        sms.leg_offset[leg][1].position(index = sms.pca_pin_number[leg][1], degrees = sms.leg_offset_angle[leg][1] + theta_2)
        sms.leg_offset[leg][2].position(index = sms.pca_pin_number[leg][2], degrees = sms.leg_offset_angle[leg][2] + theta_3 - 90)

