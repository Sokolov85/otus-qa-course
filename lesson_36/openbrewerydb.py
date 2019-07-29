"""Module with Openbrewerydb JSON API class"""
import requests


class Openbrewerydb:
    """Class with methods for requests for JSON API https://api.openbrewerydb.org"""
    def __init__(self):
        self.end_point = "https://api.openbrewerydb.org"
        self.brewery_id = 300
        self.brewery_state = "California"
        self.brewery_name = "Alosta Brewing Co"
        self.brewery_text_in_name = "dog"
        self.brewery_text_in_tag = "patio"
        self.brewery_type = "micro"

    def get_brewery(self):
        """Get breweries"""
        response = requests.get(self.end_point + '/breweries/{}'.format(self.brewery_id))
        return response.json()

    def filter_by_state(self):
        """Filter breweries list by state"""
        response = requests.get(self.end_point + '/breweries?by_state={}'.format(self.brewery_state))
        return response.json()

    def filter_by_name(self):
        """Filter breweries list by name"""
        response = requests.get(self.end_point + '/breweries?by_name={}'.format(self.brewery_name))
        return response.json()

    def autocomplete_name(self):
        """Autocomplete name"""
        response = requests.get(self.end_point + '/breweries/autocomplete?query={}'.format(self.brewery_text_in_name))
        return response.json()

    def search_name(self):
        """Brewery search by name"""
        response = requests.get(self.end_point + '/breweries?by_tag={}'.format(self.brewery_text_in_tag))
        return response.json()

    def filter_by_type(self):
        """Filter breweries list by type"""
        response = requests.get(self.end_point + '/breweries?by_type={}'.format(self.brewery_type))
        return response.json()


if __name__ == "__main__":
    brewery = Openbrewerydb()
    print(brewery.get_brewery())
    print(brewery.filter_by_state())
    print(brewery.filter_by_name())
    print(brewery.autocomplete_name())
    print(brewery.search_name())
    print(brewery.filter_by_type())
