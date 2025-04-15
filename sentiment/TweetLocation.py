
class TweetLocation:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"TweetLocation(lat={self.latitude}, lon={self.longitude})"
