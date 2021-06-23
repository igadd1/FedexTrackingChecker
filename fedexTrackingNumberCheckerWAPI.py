from fedex.config import FedexConfig
from fedex.services.track_service import FedexTrackRequest
from Utils.ResponseParser import ResponseParser
from Utils.TrackingInfo import TrackingInfo
import pandas as pd
import os, sys
import configparser
import time
import threading

def importTrackingNumbers():
    importPath = os.path.join(sys.path[0], "trackingImport.xlsx")
    importDF = pd.read_excel(importPath)

    trackingNumbers = []

    #init list of tracking numbers to check status of
    for trackingNumber in importDF['TrackingNumbers']:
        trackingNumbers.append(trackingNumber)
    return trackingNumbers

def tmpFunc(trackingNumber, trackingRequester, list, parser, numbersChecked, debug=False):
    print("Current tracking number being checked:", trackingNumber, "Checked", numbersChecked, "so far.")
    trackingRequester.SelectionDetails.PackageIdentifier.Value = trackingNumber
    trackingRequester.send_request()
    list.append(TrackingInfo(trackingRequester.response, parser))
    if debug:
        tmp = trackingRequester.response
        tmpfile = open('tmp.txt', 'w')
        tmpfile.write(str(tmp))

def sendRequests(trackingNumbers, trackingRequester, list, parser, debug=False):
    numbersChecked = 0
    for trackingNumber in trackingNumbers:
        numbersChecked +=1
        threading.Thread(target=tmpFunc, args=(trackingNumber, trackingRequester, list, parser, numbersChecked)).start()
    #sleep until all threads are closed
    while threading.active_count() > 1:
        time.sleep(.1)



def exportData(trackingObjects):
    keys = ['trackingNumber', 'packageWeight', 'sequenceNumber', 'shipperCity', 
    'actualDeliveryAddressCity','actualDeliveryAddressState', 'deliveryAttempts', 'deliverySignature',
    'eventDescription']
    d = {}
    for key in keys:
        d[key] = []
    for trackingObject in trackingObjects:
        for key in keys:
            d[key].append(getattr(trackingObject, key))
    df = pd.DataFrame.from_dict(d)
    df.to_excel(os.path.join(sys.path[0], "trackingExport.xlsx"))

def main():
    config = configparser.ConfigParser()
    config.read(os.path.join(sys.path[0], "FedexConfig.ini"))
    CONFIG_OBJ = FedexConfig(key=config['DEFAULT']['key'],password=config['DEFAULT']['password'],
    account_number=config['DEFAULT']['account_number'],meter_number=config['DEFAULT']['meter_number'],
    use_test_server=False)

    trackingInfoObjects = []
    #delete old export
    if os.path.exists(os.path.join(sys.path[0], "trackingExport.xlsx")):
        os.remove(os.path.join(sys.path[0], "trackingExport.xlsx"))
    sendRequests(importTrackingNumbers(), FedexTrackRequest(CONFIG_OBJ), 
    trackingInfoObjects, ResponseParser())
    
    exportData(trackingInfoObjects)

if __name__ == '__main__':
    startTime = time.time()
    main()
    print("Time to finish:", time.time()-startTime)