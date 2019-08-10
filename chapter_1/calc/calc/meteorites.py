from urllib.request import urlopen
import json
from calc.calc import Calc


class Meteorites():
    
    def get_data(self):

        URL = "https://data.nasa.gov/resource/y77d-th95.json"
        with urlopen(URL) as url:
            data = json.loads(url.read().decode())

        return data

    def avg_mass(self, data):
        masses = [float(d['mass']) for d in data if 'mass' in d]
            
        avg_mass = Calc().avg(masses)
        return avg_mass
    
