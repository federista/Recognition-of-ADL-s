# Recognition-of-ADL-s
<a href="https://unige.it/en/">
University Website
  
#GROUP MEMBERS
  
| Name | email  | profile |
| :--- | :---   | :--- |
| X ZAID | s4848329@studenti.unige.it | [Federista](hhttps://github.com/federista)
| Muhammad Malook Bugty | s4904540@studenti.unige.it | [Mbugti](https://github.com/mbugti)
| Mohammad Azah Hussain | s4916211@studenti.unige.it | 
| Raja Taha Hussain | s5046306@studenti.unige.it | 
| Sassi Kumar uppatala | s5058253@studenti.unige.it |
 
 ## PROJECT DESCRIPTION
 The goal of this repository is having a distributed architecture which allow user to accurately identify the activity of daily life based upon the provided dataset.
  
 ## AVAILABLE DATASET
  We have a dataset which contains data from 6 IMUs: they were placed on the volunteer’s back, left lower arm, left upper arm, right lower arm, right upper arm and right thigh.
Nine ADLs have been recorded: walking, sitting down, standing up, opening a door, closing a door, pouring water, drinking using a glass, brushing teeth and cleaning the table. 
Two distinct activity sequences have been designed and both have been performed twice using only the right hand and using only the left hand.

The first column of each IMU csv file contains a label “qags”, which indicates the type of the recorded data (i.e. quaternions, accelerometer data and gyroscope data).
The next column is the time-stamp in milliseconds elapsed from 00.00.0.000 AM (with a 30 milliseconds sampling time). The next four columns are the quaternions (with a resolution of 0.0001).The next three columns are the accelerations along the x-, y- and z-axis (with a resolution of 0.01 degrees per second).The last three columns refer to the angular velocities about the x,y and z axes (with a resolution of 0.1 mG).

Each annotations csv file’s first two columns are the current daytime in the format “hh.mm.ss.000” and in ms elapsed from 00:00:0.000 AM; the remaining columns are organized as couples where the first element represents the scope of the labelling (i.e. “BothArms”, “RightArm”, “LeftArm”, “Locomotion”) and the second indicates whether the labelled activity starts or ends.
Finally, the last two columns report as session ID.There are four different sessions characterised by the order in which the activities are performed, and by the used arm and whether the session starts or ends. The videos recorded during the experiments have been only used for labelling purposes, and they are not published.

  
  
  
  
  
