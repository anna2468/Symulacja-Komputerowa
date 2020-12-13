from Klasyprojektu import cableway, ski_lift, passenger, queue, carriage
import numpy as np

def random_passengers():
    num = np.random.randint(10)+1
    return int(num)

def simulation_cableway(new_passengers_list):
    cable = cableway(60, 10)
    q = queue()
    for i in new_passengers_list:
        q.add(i)

        cable.move_from_queue(q)
        cable.move()
        q.add_time()
    return cable.people_after

def simulation_ski_lift(new_passengers_list):
    ski = ski_lift(3, 10)
    q= queue()
    for i in new_passengers_list:
        q.add(i)

        ski.move_from_queue(q)
        ski.move()

        q.add_time()
    return ski.get_people_out()
    
def avg_time(x):
    waiting_time=0
    for i in x:
        waiting_time+=i.waiting_time
    return waiting_time/len(x)



queueList = []
for i in range(1000):
    queueList.append(random_passengers())
    


transportedPeople = simulation_cableway(queueList)
print(avg_time(transportedPeople))
transportedPeople = simulation_ski_lift(queueList)
print(avg_time(transportedPeople))