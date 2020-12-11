#!/usr/bin/env python
# coding: utf-8

class cableway():
    def __init__(self, capacity, ride_time):
        '''
        Capacity - pojemność polinki
            rodzaj - int()
        ride_time - czas przejazdu w jedną strone
            rodzaj - int()
        '''
        self.capacity = capacity                            # calkowita pojemnosc cableway
        self.ride_time = ride_time                          # czas jaki zajmuje cablewau przejechanie w jedna strone
        self.people_in = []                                 # lista ludzi aktualnie w cableway
        self.is_waiting = True                              # czy czeka na pasaerw
        self.time_traveled = 0                              # czas przejazdu (max = ride_time)
        self.people_after = []                              # lista ludzi ktorzy przejechali

    def move_from_queue(self, que):                         # funkcja zabierania z kolejki(que) pasazerow
        if self.time_traveled==0:                           # zabiera tylko jak znajduje sie w miejscu zerowym
            space_left = self.capacity-len(self.people_in)
            if space_left<=que.get_length():                # jesli jest wiecej w kolejce niz jest miejsca zabiera maksymalna liczbe osob
                self.people_in += que.queue[:space_left]
                que.queue = que.queue[space_left:]
            else:                                           # jesli jest mniej w kolejce niz sie zmiesci to zbiera wszystkich 
                self.people_in += que.queue
                que.queue = []

            if len(self.people_in)==self.capacity:          # gdy osiagnie maksymalna liczbe osob nie czeka na kolejne
                self.is_waiting = False
    
    def move(self):                                         # funkcja poruszania sie cableway
        if not self.is_waiting:                             # porusza sie tylko jak nie czeka na pasazerow
            if len(self.people_in)==self.capacity:          # jesli jest pelna to porusza sie do puktu B
                self.time_traveled+=1
                if self.ride_time==self.time_traveled:
                    people_out = self.people_in

                    self.people_in=[]
                    self.people_after += people_out
            else:                                           #jesli jest pusta wraca do punnktu A
                self.time_traveled-=1
                if self.time_traveled==0:                   # jesli jest w punkcie A to czeka na kolejnych pasazerow
                    self.is_waiting= True
        

class ski_lift():
    def __init__(self, frequency):
        ''' 
        frequency - jak często podjeżdża nowe krzesełko
            rodzaj - int()
        
        '''
        self.frequency = frequency
        
    def change_frequency(self, new_frequency):
        self.frequency = new_frequency
        
class passenger():
    def __init__(self, waiting_time=0):
        
        ''' 
        place_in_queue - miejsce w kolejce
            rodzaj - int()
        waiting_time - czas oczekiwania w danym momencie
            rodzaj - int()
        '''
        self.waiting_time = waiting_time
        
    def move(self):
        self.place_in_queue = self.place_in_queue - 1
        
        if self.place_in_queue == 0:
            time_in_queue = self.waiting_time
            
            return f'Waiting time = {time_in_queue}', time_in_queue
        
    def add_time(self):
        self.waiting_time = self.waiting_time + 1
        
class queue():
    def __init__(self, queue=[]):
        self.queue = queue
        
    def add(self, number_of_passengers):                # dodanie pewnej liczby ludzi do kolejki
        for _ in range(number_of_passengers):
            self.queue.append(passenger())

    def get_length(self):
        return len(self.queue)

    def add_time(self):                     # dodanie jednej jednostki czasu dla wszystkich czlonkow kolejki
        for i in self.queue:
            i.add_time()
