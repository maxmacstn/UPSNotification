import serial
import requests


#Virtual port
SERIAL_PORT = 'COM3'
# be sure to set this to the same rate used on the ViewPower configuration webpage
SERIAL_RATE = 9600

#Line API settings
url = 'https://notify-api.line.me/api/notify'
tokens = ['YOUR TOKEN HERE']




def sendNotification(text):
    for token in tokens:
        headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=headers, data={'message': text})
        print("Sent notification " + r.text)



def parseInput(rawString):
    if "Event:" in rawString:
        sendNotification(rawString)



def main():
    count = 0;
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    while True:
        # using ser.readline() assumes each line contains a single reading
        # sent using Serial.println() on the Arduino
        reading = ser.readline().decode('utf-8')
        # reading is a string...do whatever you want from here
        print(reading)
        parseInput(reading)


if __name__ == "__main__":
    main()