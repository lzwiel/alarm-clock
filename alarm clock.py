import datetime
import time
import playsound

alarm_time = input("请输入闹钟时间（格式：HH:MM:SS）：")
alarm_hour = alarm_time[:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]

while True:
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second
    
    if (current_hour == int(alarm_hour)) and (current_minute == int(alarm_minute)) and (current_second == int(alarm_second)):
        print("时间到！")
        playsound.playsound('alarm.wav')
        break
    else:
        print("等待中...")
        time.sleep(1)
        
        请注意，在运行此代码之前，您必须安装playsound模块，并且需要将一个名为alarm.wav的音频文件放置在与您的代码文件相同的文件夹中。
