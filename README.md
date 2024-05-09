Project for developing an autonomous navigation stack for Clearpath Jackal UGV (https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/) to facilitate autonomous scanning of construction areas. This automation is a replacement for human performing manual inspection and can help identify any issues with the construction site without putting a human in danger.

<!-- ![High level architecture for autonomous navigation](assets\High_level_Arch.png) -->
<img src="assets\High_level_Arch.png" alt="High level architecture for autonomous navigation" width="600" height="400">


This project was the result of a collaboration of 2 teams, the UGV team and the Kinova Arm team. 
- The UGV team, the team of which I was a part of developed the autnomous navigation stack using RTABMAP SLAM algorithm for mapping, move base for navigation and Yolov7 for real-time obstacle detection and rerouting by integration with move base costmap.
- The UGV team utilized RGBD camera for mapping and navigation. All the algorithms were deployed on Jetson Nano which was also used for communicating with the Kinova team's Jetson Nano.
- The Kinova team communicated with the UGV through ROS based python scripts to start and stop 3D scanning of objects of interest with an RGBD camera.  

The UGV team worked on the following:
1. Mapping of the area of interest. For this we utilized RTABMAP SLAM algorithm in ROS melodic.
<!-- ![Generated Map from RATBMAP SLAM](assets\wrong_localization.jpg) -->
<img src="assets\wrong_localization.jpg" alt="Generated Map from RATBMAP SLAM" width="600" height="400">

2. Navigation with Movebase and Yolov7 integration.
<!-- ![Navigation](assets\move_base_rviz.png) -->
<img src="assets\move_base_rviz.png" alt="Navigation" width="600" height="400">

3. Communication and coordination with the Kinova Arm team
<!-- ![Communication with Kinova arm](assets\flow.png) -->
<img src="assets\flow.png" alt="Communication with Kinova arm" width="600" height="400">


A small demo of the project illustrating the autonmous navigation can be seen below:

<video width="600" height="400" controls>
  <source src="assets/Navigation and communication demo.mp4" type="video/mp4">
</video>