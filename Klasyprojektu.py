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
    def __init__(self, capacity, ride_time, frequency=1):
        ''' 
        frequency - jak często podjeżdża nowe krzesełko (2*ride_time%frequency==0)
            rodzaj - int()
        
        '''
        self.frequency = frequency
        self.number_of_carriages = int(2*ride_time/frequency)
        self.capacity = capacity
        self.ride_time = ride_time
        self.carriages = []
        back = False
        for i in range(self.number_of_carriages):
            if i*frequency<self.ride_time:
                self.carriages.append(carriage(self.capacity, self.ride_time, i*frequency,back))
            else:
                back=True
                self.carriages.append(carriage(self.capacity, self.ride_time, (self.ride_time-((i*frequency)-self.ride_time)),back))
    
    def move_from_queue(self, que):
        for i in self.carriages:
            i.move_from_queue(que)
    
    def move(self):
        for i in self.carriages:
            i.move()

    def get_people_out(self):
        out = []
        for i in self.carriages:
            out+=i.people_out
        return out
class carriage():
    def __init__(self, capacity, ride_time, time_traveled = 0, back = False):
        self.capacity = capacity
        self.ride_time = ride_time
        self.time_traveled = time_traveled
        self.people_in = []
        self.back = back
        self.people_out = []

    def move_from_queue(self, que):
        if self.time_traveled == 0:
            if self.capacity<=que.get_length():
                self.people_in = que.queue[:self.capacity]
                que.queue = que.queue[self.capacity:]
            else:
                self.people_in = que.queue
                que.queue = []

    def move(self):
        if self.back:
            self.time_traveled-=1
            if self.time_traveled==0:
                self.back=False
        else:
            self.time_traveled+=1
            if self.time_traveled==self.ride_time:
                self.people_out += self.people_in
                self.people_in = []
                self.back=True

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
