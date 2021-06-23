class ResponseParser():
    def __init__(self):
        pass
    def getTrackingNumber(self, response):
        try:
            res = response['CompletedTrackDetails'][0]['TrackDetails'][0][1]
        except:
            res = "None"
        return res
    def getPackageWeight(self, response):
        try:
            res = response['CompletedTrackDetails'][0]['TrackDetails'][0]['PackageWeight']['Value']
        except:
            res = "None"
        return res
    def getPackageSequenceNumber(self, response):
        try:
            res = response['CompletedTrackDetails'][0]['TrackDetails'][0]['PackageSequenceNumber']
        except:
            res = "None"
        return res

    def getShipperCity(self, response):
        try:
            res = response['CompletedTrackDetails'][0]['TrackDetails'][0]['ShipperAddress']['City']
        except:
            res = "None"
        return res

    def getShipperState(self, response):
        try:
            res = response['CompletedTrackDetails'][0]['TrackDetails'][0]['ShipperAddress']['City']
        except:
            res = "None"
        return res

    def getShipperCountryCode(self, response):
        try:
            res = response['CompletedTrackDetails'][0]['TrackDetails'][0]['ShipperAddress']['CountryCode']
        except:
            res = "None"
        return res

    def getActualDeliveryAddressCity(self, response):
        try:
            res = response['CompletedTrackDetails'][0]['TrackDetails'][0]['ActualDeliveryAddress']['City']
        except:
            res = "None"
        return res

    def getActualDeliveryAddressState(self, response):
        try:
            res = response['CompletedTrackDetails'][0]['TrackDetails'][0]['ActualDeliveryAddress']['StateOrProvinceCode']
        except:
            res = "None"
        return res

    def getActualDeliveryAddressCountryCode(self, response):
        try:
            res = response['CompletedTrackDetails'][0]['TrackDetails'][0]['ActualDeliveryAddress']['CountryCode']
        except:
            res = "None"
        return res
    def getDeliveryAttempts(self, response):
        try:
            res = response['CompletedTrackDetails'][0]['TrackDetails'][0]['DeliveryAttempts']
        except:
            res = "None"
        return res
    
    def getDeliverySignature(self, response):
        try:
            res = response['CompletedTrackDetails'][0]['TrackDetails'][0]['DeliverySignatureName']
        except:
            res = "None"
        return res
    
    def getEventDescription(self, response):
        try:
            res = response['CompletedTrackDetails'][0]['TrackDetails'][0]['Events'][0]['EventDescription']
        except:
            res = "None"
        return res