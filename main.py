from prettytable import PrettyTable
import tts
import getTrainData
import time
import json


def get_sec(time_str):
    """Get seconds from time."""
    time = time_str.split(':')
    return int(time[0]) * 3600 + int(time[1]) * 60

def main(): 
    tts.speakFaster("The TrainTTS script has now started. This is the volume of voice to be currently used, please adjust it to your liking.")
    tts.speakFaster("Please enter the STATION NAME you would like to monitor")

    stationName = input("Please enter the NAME of the STATION you would like to monitor: ")
    stationCode = input("Please enter the CODE of the STATION you would like to monitor: ")

    tts.speak("The Selected station is " + stationName + " and the code is " + stationCode)

    monitorStation(stationName, stationCode)

def monitorStation(stationName, stationCode):
    # tts.speak("Now starting to monitor the selected station. Passing and Departing/Arriving trains will all be spoken.")

    startTime = time.perf_counter()
    hasDeparturesListBeenShown = False

    listOfPassingTrains = json.loads(getTrainData.getPassingTrains(stationCode).text)
    listOfDepartingTrains = json.loads(getTrainData.getDepartingTrains(stationCode).text)

    passingTrains = listOfPassingTrains['passes']['all']
    departingTrains = listOfDepartingTrains['departures']['all']


    lastPassingTrainHeadcode = 'eeeeeeeeeeeeeeeeee'
    lastDepartingTrainHeadcode = 'eeeeeeeeeeeeeee'
    while True:
        # Time to 24-hour clock
        currentTime = time.strftime('%H:%M')
        if(time.perf_counter() - startTime == 60*2.5 or hasDeparturesListBeenShown == False):
            hasDeparturesListBeenShown = True
            print("Refreshing Trains list")
            listOfPassingTrains = json.loads(getTrainData.getPassingTrains(stationCode).text)
            listOfDepartingTrains = json.loads(getTrainData.getDepartingTrains(stationCode).text)

            passingTrains = listOfPassingTrains['passes']['all']
            departingTrains = listOfDepartingTrains['departures']['all']

            print("Departures in the next five minutes")
            t = PrettyTable(['Headcode', 'Operator', 'Destination', 'Origin', 'Passing/Stopping', 'Status', 'Arrival', 'Departure', 'Expected Arrival'])

            for i in departingTrains:
                # if train is arriving in the next 2.5 minutes

                if(i['mode'] != 'train'):
                    continue
                if(i['expected_arrival_time'] is None):
                    i['expected_arrival_time'] = i['aimed_departure_time']
                if(get_sec(i['expected_arrival_time']) - get_sec(currentTime) <= 60*5):
                    t.add_row([i['train_uid'], i['operator_name'], i['destination_name'], i['origin_name'], i['status'], i['aimed_pass_time'], i['aimed_arrival_time'], i['aimed_departure_time'], i['expected_arrival_time']])
            print(t)


            tb = PrettyTable(['Headcode', 'Operator', 'Destination', 'Origin', 'Passing/Stopping', 'Status', 'Arrival', 'Departure', 'Expected Arrival'])
            print("Passing Trains in the next five minutes")
            for i in passingTrains:
                if(i['mode'] != 'train'):
                    continue
                if(i['aimed_pass_time'] is None):
                    continue
                # if train is arriving in the next 2.5 minutes
                if(get_sec(i['aimed_pass_time']) - get_sec(currentTime) <= 60*5):
                    t.add_row([i['train_uid'], i['operator_name'], i['destination_name'], i['origin_name'], i['status'], i['aimed_pass_time'], i['aimed_arrival_time'], i['aimed_departure_time'], i['expected_arrival_time']])
            print(tb)
            startTime = time.perf_counter()
        

        # Check if there are any passing trains at this moment

        for i in passingTrains:
            if(i['aimed_pass_time'] == currentTime):
                if(i['service_timetable']['id'] != lastPassingTrainHeadcode):
                    lastPassingTrainHeadcode = i['service_timetable']['id']

                    
                    t = PrettyTable(['Headcode', 'Operator', 'Destination', 'Origin', 'Passing/Stopping', 'Status', 'Arrival', 'Departure', 'Expected Arrival'])
                    t.add_row([i['train_uid'], i['operator_name'], i['destination_name'], i['origin_name'], i['status'], i['aimed_pass_time'], i['aimed_arrival_time'], i['aimed_departure_time'], i['expected_arrival_time']])
                    print(t)

                    tts.speak("The "+ i['aimed_pass_time'].replace(":", '') + i['operator_name'] + " to " + i['destination_name'] + "is now passing " + stationName + " from " + i['origin_name'] + " the train is" + i['status'] + "Headcode: " + i['train_uid'])

                    break

        for i in departingTrains:
            if(i['expected_arrival_time'] == currentTime):
                if(i['service_timetable']['id'] != lastDepartingTrainHeadcode):
                    print("""
                    ░▀█▀▒█▀▄▒▄▀▄░█░█▄░█░░▒▄▀▄▒█▀▄▒█▀▄░█░█▒█░█░█▄░█░▄▀▒
                    ░▒█▒░█▀▄░█▀█░█░█▒▀█▒░░█▀█░█▀▄░█▀▄░█░▀▄▀░█░█▒▀█░▀▄█
                    """)
                    lastDepartingTrainHeadcode = i['service_timetable']['id']
                    t = PrettyTable(['Headcode', 'Operator', 'Destination', 'Origin', 'Passing/Stopping', 'Status', 'Arrival', 'Departure', 'Expected Arrival'])
                    t.add_row([i['train_uid'], i['operator_name'], i['destination_name'], i['origin_name'], i['status'], i['aimed_pass_time'], i['aimed_arrival_time'], i['aimed_departure_time'], i['expected_arrival_time']])
                    print(t)
                    tts.speak("The train now approaching platform " + i['platform'] + " is the " + i['aimed_arrival_time'].replace(":", '') + i['operator_name'] + " to " + i['destination_name'] + " from " + i['origin_name'] + " the train is" + i['status'] + "with the headcode: " + i['train_uid'])

                    break





# main()
main()