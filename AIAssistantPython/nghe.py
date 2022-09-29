from email.mime import audio
import speech_recognition

robot_ear = speech_recognition.Recognizer() # Tạo tai nghe cho robot
with speech_recognition.Microphone() as mic: 
#mic = speech_regcognition.Microphone() giống với dòng trên nhưng mic ở đây không bị tắt sau khi thực thi tác vụ.
    print("Robot: I'm Listening")
    audio = robot_ear.listen(mic)

you = robot_ear.recognize_google(audio) #Tai nhận dạng và nghe âm thanh
#Sửa runtime error
try: 
    you = robot_ear.recognize_google(audio)
except:
    you = ""

print("You: " + you)
