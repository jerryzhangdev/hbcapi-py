import requests
class access:
    def __init__(self, auth):
        ''' Constructor for this class. '''
        # Create some member animals
        self.auth = auth
        
 
 
    def poststats(self, guildcount):
        headers = { "Authorization": str(self.auth), "guildcount": str(guildcount) }
        r = requests.post("https://hydrogenbots.club/api/v1/servercount", headers=headers)
        return r.content

    def voters(self):
        headersforvoter = { "Authorization": str(self.auth) }
        r = requests.get("https://hydrogenbots.club/api/v1/voters", headers=headersforvoter)
        return r.content