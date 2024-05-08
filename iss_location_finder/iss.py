import requests

class GetData():
    def __init__(self, url):
        self.url = url
        self.response = 'empty response'

    def get_response(self):
        return requests.get(self.url).json()
    

class ReturnLocation(GetData):

    def print_location(self):
        pass


        


    