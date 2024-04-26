#!/usr/bin/env python
# license removed for brevity

import rospy
from sensor_msgs.msg import Imu

def imu_callback(msg):
    # Crie uma nova mensagem IMU modificada
    modified_msg = Imu()


    modified_msg.header = msg.header

    modified_msg.orientation.x = -msg.orientation.y
    modified_msg.orientation.y = -msg.orientation.z
    modified_msg.orientation.z = msg.orientation.x  
    modified_msg.orientation.w = msg.orientation.w

 
    modified_msg.angular_velocity.x = -msg.angular_velocity.y
    modified_msg.angular_velocity.y = -msg.angular_velocity.z
    modified_msg.angular_velocity.z = msg.angular_velocity.x
  
    modified_msg.linear_acceleration.x = -msg.linear_acceleration.y
    modified_msg.linear_acceleration.y = -msg.linear_acceleration.z
    modified_msg.linear_acceleration.z = msg.linear_acceleration.x
    
    
    # Publique a mensagem modificada no tópico desejado
    pub.publish(modified_msg)

if __name__ == '__main__':
    rospy.init_node('imu_modifier_axes')

    # Subscreva ao tópico de IMU
    rospy.Subscriber('/Pionner/D435i_camera/imu/sample', Imu, imu_callback)

    # Crie um publicador para a mensagem IMU modificada
    pub = rospy.Publisher('/Pionner/D435i_camera/imu/modified', Imu, queue_size=10)

    # Mantenha o nó em execução
    rospy.spin()
