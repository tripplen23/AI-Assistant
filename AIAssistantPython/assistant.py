from email.mime import audio
import speech_recognition
import pyttsx3
from datetime import date, datetime




robot_ear = speech_recognition.Recognizer() # Tạo tai nghe cho robot
robot_mouth = pyttsx3.init() # Tạo miệng cho robot
robot_brain = ""

while True:
    #Listen

    with speech_recognition.Microphone() as mic: 
    #mic = speech_regcognition.Microphone() giống với dòng trên nhưng mic ở đây không bị tắt sau khi thực thi tác vụ.
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)

    print("Robot: ...")
    #Sửa runtime error
    try: 
        you = robot_ear.recognize_google(audio) #Tai nhận dạng và nghe âm thanh
    except:
        you = ""

    print("You: " + you)

    #Understand
    if you == "":
        robot_brain = "Sorry, I can't hear you"
    elif "my love" in you:
        robot_brain = "Linh Lu"
    elif "hello" in you:
        robot_brain = "Hello Binh Nguyen"
    elif "today" in you:
        today = date.today()
        # Textual month, day and year	
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        # Textual month, day and year
        # current_time = now.strftime("%H hours %M minutes %S seconds")	
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "president" in you:
        robot_brain = "Joe Biden"
    elif "who are you" "your name" in you:
        robot_brain = "I am your assistant"
    elif "good job" in you:
        robot_brain = "Thank you very much"       
    elif "bye" in you: 
        robot_brain = "Bye Binh Nguyen"    
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait() #say bye :'(
        break
    else:
        robot_brain = "I'm fine thank you, and you?"
    print("Robot: " + robot_brain)

    #Say
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()