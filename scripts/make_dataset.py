#!/usr/bin/env python3
import os
import sys
import argparse

import rospy
import roslib
roslib.load_manifest('ptp_make_dataset')
import numpy as np
from ptp_msgs.msg import PedestrianArray

class MakeDataset():
    def __init__(self):
        rospy.init_node('make_dataset_node', anonymous=True)
        self.curr_ped_sub = rospy.Subscriber(
            '/curr_ped',
            PedestrianArray,
            self.curr_ped_callback)

        if not rospy.has_param('tag'):
            rospy.set_param('tag', 'hoge')
        self.tag = rospy.get_param('tag')

        self.pkg_path = roslib.packages.get_pkg_dir('ptp_make_dataset')

        dataset_dir = self.pkg_path + '/datasets/' + self.tag + '/'

        if not os.path.exists(dataset_dir):
            os.makedirs(dataset_dir)
        
    def curr_ped_callback(self, msg):
        data_array = np.array(msg.data, dtype=np.dtype(msg.dtype)).reshape(msg.shape)
        self.add_data(data_array)

    def add_data(self, data_array_):
        pass
    
    def loop(self):
        pass

def main():
    node = MakeDataset()
    rospy.spin()

if __name__ == '__main__':
    main()
