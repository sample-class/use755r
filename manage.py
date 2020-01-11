from data import tours

class Manage():

    def __init__(self):
        pass

    def depart_city (self, direction):

        tour_departure = {}
        for id_tour, tour_info in tours.items():
            if tour_info["departure"] == direction:
                tour_departure[id_tour]=tour_info
        return (tour_departure)



