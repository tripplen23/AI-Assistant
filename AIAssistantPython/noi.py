import pyttsx3

robot_brain = "Thank you very much"

robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()