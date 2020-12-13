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
        self.capacity = capacity
        self.ride_time = ride_time

        
    def add_passenger(self):
        if self.capacity == 0:
            return f'The cableway is full'
        self.capacity = self.capacity - 1

    def change_ridetime(self, new_ride_time):
        self.ride_time = new_ride_time

    def change_capacity(self, new_capacity):
        self.capacity = new_capacity
        
        
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
    def __init__(self, place_in_queue, waiting_time):
        
        ''' 
        place_in_queue - miejsce w kolejce
            rodzaj - int()
        waiting_time - czas oczekiwania w danym momencie
            rodzaj - int()
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
        
class queue():
    def __init__(self, queue):
        self.queue = []
        
    def add(self, passenger):
        self.queue.append(passenger(get_length(self.queue), 0))

    def pop(self):        
        first_passanger = self.lenght.pop(0)
        for passenger in self.queue:
            passenger.move()
        
        return first_passenger
        
    def get_length(self):
        return len(self.queue)
    
