from time import sleep
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

YES = "up"
NO = "down"
MEASURE_TEXT = "Measures:"

Temp_Colors = [[255, 0, 0], [0, 0, 0]]
Press_Colors = [[0, 255, 0], [0, 0, 0]]
Humi_Colors = [[0, 0, 255], [0, 0, 0]]


def get_datetime():
    return datetime.now().strftime("%m/%d/%Y,%H:%M:%S,")


def JoyStick_Event():
    event = sense.stick.wait_for_event(emptybuffer=True)
    return event.action, event.direction


def Temperature():
    Measurements = []

    Measure_Count = 0

    sense.show_message(MEASURE_TEXT, text_colour=Temp_Colors[0], scroll_speed=0.05, back_colour=Temp_Colors[1])
    sense.show_letter("0", text_colour=Temp_Colors[0], back_colour=Temp_Colors[1])
    accepted = False
    while not accepted:
        event = JoyStick_Event()
        if event[1] == "left" and Measure_Count > 0 and event[0] != "pressed":
            Measure_Count -= 1
            sense.show_letter(str(Measure_Count), text_colour=Temp_Colors[0], back_colour=Temp_Colors[1])
        elif event[1] == "right" and event[0] != "pressed":
            Measure_Count += 1
            sense.show_letter(str(Measure_Count), text_colour=Temp_Colors[0], back_colour=Temp_Colors[1])
        elif event[1] == YES:
            accepted = True
        elif event[1] == NO:
            return
    sleep(1)
    for _ in range(Measure_Count):
        temp = sense.get_temperature()
        sense.show_message(str(round(temp, 2)) + " C", text_colour=Temp_Colors[0], back_colour=Temp_Colors[1],
                           scroll_speed=0.04)
        Measurements.append(get_datetime() + str((round(temp, 2))))
        sleep(1)
    if len(Measurements) != 0:
        avg = sum(map(lambda x: float(x.split(",")[2]), Measurements)) / len(Measurements)
        sense.show_message("Average: ", text_colour=Temp_Colors[0], back_colour=Temp_Colors[1], scroll_speed=0.05)
        if avg >= 20:
            sense.show_message(str(avg) + " C" + " HOT", text_colour=Temp_Colors[0], back_colour=Temp_Colors[1],
                               scroll_speed=0.05)

        elif avg < 20 and temp >= 15:
            sense.show_message(str(avg) + " C" + " PERFECT", text_colour=Temp_Colors[0], back_colour=Temp_Colors[1],
                               scroll_speed=0.05)

        elif temp < 15:
            sense.show_message(str(avg) + " C" + " COLD", text_colour=Temp_Colors[0], back_colour=Temp_Colors[1],
                               scroll_speed=0.05)

    if len(Measurements) != 0:
        sense.show_message("Save?", text_colour=Temp_Colors[0], back_colour=Temp_Colors[1], scroll_speed=0.05)
        answer = JoyStick_Event()
        if answer[1] == YES and answer[0] == "pressed":
            sense.show_message("Saving...", text_colour=Temp_Colors[0], back_colour=Temp_Colors[1], scroll_speed=0.05)
            file = open("temps.txt", "a")
            for line in Measurements:
                file.write(line + "\n")
            file.close()
            sense.show_message("Saved", text_colour=Temp_Colors[0], back_colour=Temp_Colors[1], scroll_speed=0.05)
    return


def Pressure():
    Measurements = []
    Measure_Count = 0
    sense.show_message(MEASURE_TEXT, text_colour=Press_Colors[0], scroll_speed=0.05, back_colour=Press_Colors[1])
    sense.show_letter("0", text_colour=Press_Colors[0], back_colour=Press_Colors[1])
    accepted = False
    while not accepted:
        event = JoyStick_Event()

        if event[1] == "left" and Measure_Count > 0 and event[0] != "pressed":
            Measure_Count -= 1
            sense.show_letter(str(Measure_Count), text_colour=Press_Colors[0], back_colour=Press_Colors[1])
        elif event[1] == "right" and event[0] != "pressed":
            Measure_Count += 1
            sense.show_letter(str(Measure_Count), text_colour=Press_Colors[0], back_colour=Press_Colors[1])
        elif event[1] == YES:
            accepted = True
        elif event[1] == NO:
            return

    for _ in range(Measure_Count):
        press = sense.get_pressure()
        sense.show_message(str(round(press)), text_colour=Press_Colors[0], back_colour=Press_Colors[1],
                           scroll_speed=0.04)

        Measurements.append(get_datetime() + str((round(press))))
        sleep(1)
    if len(Measurements) != 0:
        sense.show_message("Save?", text_colour=Press_Colors[0], back_colour=Press_Colors[1], scroll_speed=0.05)
        answer = JoyStick_Event()
        if answer[1] == YES and answer[0] == "pressed":
            file = open("pressures.txt", "a")
            sense.show_message("Saving...", text_colour=Press_Colors[0], back_colour=Press_Colors[1], scroll_speed=0.05)
            for line in Measurements:
                file.write(line + "\n")
            file.close()
            sense.show_message("Saved", text_colour=Press_Colors[0], back_colour=Press_Colors[1], scroll_speed=0.05)
    return


def Humidity():
    Measurements = []
    Measure_Count = 0
    sense.show_message(MEASURE_TEXT, text_colour=Humi_Colors[0], scroll_speed=0.05, back_colour=Humi_Colors[1])
    sense.show_letter("0", text_colour=Humi_Colors[0], back_colour=Humi_Colors[1])
    accepted = False
    while not accepted:
        event = JoyStick_Event()

        if event[1] == "left" and Measure_Count > 0 and event[0] != "pressed":
            Measure_Count -= 1
            sense.show_letter(str(Measure_Count), text_colour=Humi_Colors[0], back_colour=Humi_Colors[1])
        elif event[1] == "right" and event[0] != "pressed":
            Measure_Count += 1
            sense.show_letter(str(Measure_Count), text_colour=Humi_Colors[0], back_colour=Humi_Colors[1])
        elif event[1] == YES:
            accepted = True
        elif event[1] == NO:
            return

    for _ in range(Measure_Count):
        hum = sense.get_humidity()
        sense.show_message(str(round(hum, 2)) + "%", text_colour=Humi_Colors[0], back_colour=Humi_Colors[1],
                           scroll_speed=0.04)
        Measurements.append(get_datetime() + str((round(hum))) + "%")
        sleep(1)
    if len(Measurements) != 0:
        sense.show_message("Save?", text_colour=Humi_Colors[0], back_colour=Humi_Colors[1], scroll_speed=0.05)
        answer = JoyStick_Event()
        if answer[1] == YES and answer[0] == "pressed":
            file = open("humidity.txt", "a")
            sense.show_message("Saving...", text_colour=Humi_Colors[0], back_colour=Humi_Colors[1], scroll_speed=0.05)
            for line in Measurements:
                file.write(line + "\n")
            file.close()
            sense.show_message("Saved", text_colour=Humi_Colors[0], back_colour=Humi_Colors[1], scroll_speed=0.05)
    return


def add(last):
    if last == 2:
        return 0
    else:
        return last + 1


def sub(last):
    if last == 0:
        return 2
    else:
        return last - 1

def display(opt):
    if opt == "T":
        sense.show_letter("T", text_colour=Temp_Colors[0], back_colour=Temp_Colors[1])
    elif opt == "P":
        sense.show_letter("P", text_colour=Press_Colors[0], back_colour=Press_Colors[1])
    elif opt == "H":
        sense.show_letter("H", text_colour=Humi_Colors[0], back_colour=Humi_Colors[1])

def menu():
    Functions = [Temperature, Pressure, Humidity]
    Options = ["T", "P", "H"]
    OPT = 0
    User_Choice = None
    sense.show_message("MENU", text_colour=[255, 0, 0], scroll_speed=0.04)
    display("T")
    while True:
        event = JoyStick_Event()
        if event[1] == "left":
            OPT = sub(OPT)
            display(Options[OPT])
            User_Choice = Functions[OPT]
        elif event[1] == "up" and User_Choice:
            User_Choice()
            sense.show_message("MENU", text_colour=[255, 0, 0], scroll_speed=0.04)
            display(Options[OPT])
        elif event[1] == "right":
            OPT = add(OPT)
            display(Options[OPT])
            User_Choice = Functions[OPT]
        elif event[1] == "down":
            sense.show_message("Exit?", text_colour=[255, 0, 0], scroll_speed=0.04)
            event = JoyStick_Event()
            if event[1] == "up":
                sense.show_message("Bye!", text_colour=[255, 0, 0], scroll_speed=0.04)
                break
        sleep(0.25)
menu()