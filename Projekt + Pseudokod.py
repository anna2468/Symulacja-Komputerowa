import numpy as np

class cableway():
    def __init__(self, capacity, ride_time):
        
        '''
        Capacity - pojemność polinki
        rodzaj - int()
        ride_time - czas przejazdu w jedną strone
        rodzaj - int()
        
        '''
        
        self.capacity = capacity
        self.ride_time = ride_time
        self.cableway = []
        
    def add_passenger(self, passenger):
        if self.capacity <= len(self.cableway):
            return f'The cableway is full'
        if passenger in self.cableway:
            return f'Passanger is already in'

        self.cableway.append(passenger)    
        
    def change_ridetime(self, new_ride_time):
        self.ride_time = new_ride_time
        
    def change_capacity(self, new_capacity):
        self.capacity = new_capacity
        
    def show(self):
        return str(self.cableway)
        
    def get_avg_time(self):
        times = []
        for i in self.cableway:
            times.append(i.get_time())
                    
        return np.average(times)
    
    def get_all_times(self):
        for i in self.cableway:
            print(i.get_time())
            
    def reset_cableway(self):
        self.cableway = []
        
    def ride(self):
        for i in self.cableway:
            iteration = 0
            while self.ride_time != iteration:
                i.add_time()
                iteration = iteration + 1

    def is_full(self):
        if self.capacity == len(self.cableway):
            return True
        return False
    
    def info(self):
        pass
        
class ski_lift():
    def __init__(self, frequency, ride_time):
        self.frequency = frequency
        self.ride_time = ride_time
        self.ski_lift = []
        
        
        ''' 
        frequency - jak często podjeżdża nowe krzesełko
        rodzaj - int()
        
        '''
        
        self.frequency = frequency
        
    def change_frequency(self, new_frequency):
        self.frequency = new_frequency
        
    def add_passenger(self, passenger):
        iteration = 0
        while ride_time != iteration:
            passener.add_time()
            iteration = iteration + 1
            
        self.ski_lift.append(passenger)
        
    def get_avg_time(self):
        times = []
        for i in self.ski_lift:
            times.append(i.get_time())
            
        return np.average(times)
        
        
class passenger():
    def __init__(self, place_in_queue, waiting_time):
        
        ''' 
        place_in_queue - miejsce w kolejce
        rodzaj - int()
        
        waiting_time - czas oczekiwania w danym momencie
        
        '''
        
        self.place_in_queue = place_in_queue
        self.waiting_time = waiting_time
        
    def move(self):
        self.place_in_queue = self.place_in_queue - 1
        
        if self.place_in_queue == 0:
            time_in_queue = self.waiting_time
            
            return f'Waiting time = {time_in_queue}', time_in_queue
        
    def add_time(self):
        self.waiting_time = self.waiting_time + 1
        
    def add_place(self, place):
        self.place_in_queue = place
        
    def get_place(self):
        return int(self.place_in_queue)
    
    def get_time(self):
        return int(self.waiting_time)    
    
class queue():
    def __init__(self):
        self.queue = []
        
    def add_passenger(self, passenger):
        if len(self.queue) == 0:
            self.queue.append(passenger)
            passenger.add_place(len(self.queue))
        else:
            for i in self.queue:
                i.add_time()
            self.queue.append(passenger)
            passenger.add_place(len(self.queue))

    def pop(self):        
        first_passenger = self.queue.pop(0)
        first_passenger.move()
        for i in self.queue:
            i.move()
        #Dodaj zmiane miejsca w kolejce
        return first_passenger
        
    def get_length(self):
        return len(self.queue)
    
    def show(self):
        pass
    
    def get_all_times(self):
        for i in self.queue:
            i.get_time()
            
    def get_all_places(self):
        for i in self.queue:
            print(i.get_place())
            
    def info(self):
        iteration = 1
        print(f'Dlugosc kolejki: {len(self.queue)} \n')
        for i in self.queue:
            print(f'Pasażer nr: {iteration}:')
            print(f'Numer w kolejce: {i.get_place()}')
            print(f'Czas oczekiwania: {i.get_time()}')
            iteration = iteration + 1
            
        print('\n \n')

polinka = cableway(3, 2)
kolejka = queue()
p1 = passenger(0, 0)
p2 = passenger(0, 0)
p3 = passenger(0, 0)
p4 = passenger(0, 0)

kolejka.add_passenger(p1)
kolejka.add_passenger(p2)
kolejka.add_passenger(p3)
kolejka.add_passenger(p4)


kolejka.info()

p1 = kolejka.pop()
p2 = kolejka.pop()
p3 = kolejka.pop()
p4 = kolejka.pop()

polinka.add_passenger(p1)
polinka.add_passenger(p2)
polinka.add_passenger(p3)

polinka.get_all_times()
polinka.ride()

polinka.get_all_times()
polinka.get_avg_time()

# Pseudokod dla polinki

# Czas symulacji 
# Dopoki czas to symuluj
#     Czy ktos dochodzi do kolejki:
#         jesli tak:
#             dodajemy do kolejki
#             dodajemy czas dla kazdego oczekujacego
            
#         jesli nie:
#             dodajemu czas dla kazdego oczekujacego
    
#     Jesli polinka jest pełna:
#         jesli tak:
#             polinka rusza
#             dla kazdego w kolejce:
#                 dodaj czas przejazdu polinki x2
#         jesli nie:
#             przesuwamy kolejke
#             dodajemy pasazera do polinki
#     czas symulacji =- 1

# Pseudokod dla wyciagu

# dopoki czas to symuluj:
#     Czy ktos dochodzi do kolejki:
#         jesli tak:
#             dodajemy do kolejki
#             dodajemy czas dla kazdego oczekujacego

#         jesli nie:
#             dodajemu czas dla kazdego oczekujacego
    
#     dodaj do wyciagu
#     dodaj pasazerowi czas przejazdu
#     przesun kolejke

