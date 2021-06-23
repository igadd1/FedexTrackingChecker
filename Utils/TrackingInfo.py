class TrackingInfo():
    def __init__(self, response, parser):
        self.response = response
        self.trackingNumber = parser.getTrackingNumber(self.response)
        self.packageWeight = parser.getPackageWeight(self.response)
        self.sequenceNumber = parser.getPackageSequenceNumber(self.response)
        self.shipperCity = parser.getShipperCity(self.response)
        self.shipperState = parser.getShipperState(self.response)
        self.actualDeliveryAddressCity = parser.getActualDeliveryAddressCity(self.response)
        self.actualDeliveryAddressState = parser.getActualDeliveryAddressState(self.response)
        self.deliveryAttempts = parser.getDeliveryAttempts(self.response)
        self.deliverySignature = parser.getDeliverySignature(self.response)
        self.eventDescription = parser.getEventDescription(self.response)