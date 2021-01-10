from Klasyprojektu import cableway, ski_lift, passenger, queue, carriage
import numpy as np

def random_passengers_rownomierny(n):
    num = np.random.randint(n+1)
    return int(num)

def random_passengers_normal(n):
    num = np.random.normal()+n
    if int(num)>=0:
        return int(num)
    else:
        return 0

def simulation_cableway(new_passengers_list, czas_przejazdu=10, miejsca_w_polince=60):
    cable = cableway(miejsca_w_polince, czas_przejazdu)
    q = queue()
    for i in new_passengers_list:
        q.add(i)

        cable.move_from_queue(q)
        cable.move()
        q.add_time()
    return cable.people_after

def simulation_ski_lift(new_passengers_list, czas_przejazdu=10, miejsca_w_wagonie=5):
    ski = ski_lift(miejsca_w_wagonie, czas_przejazdu, 1)
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

#oba zminan kolejki 1-10
polinka = []
ski = []
for n in range(10):
    q=[]
    for _ in range(1000):
        q.append(random_passengers_rownomierny(n+1))
    c = simulation_cableway(q)
    sl = simulation_ski_lift(q)
    polinka.append(avg_time(c))
    ski.append(avg_time(sl))
for i in range(len(polinka)):
    print("Polinka kolejka ", i+1, ": ", polinka[i])
for i in range(len(ski)):
    print("Wagony kolejka ", i+1, ": ", ski[i])

print(30*'#')

#oba zmiana kolejki rownomierny norm
norm = []
for _ in range(1000):
    norm.append(random_passengers_normal(6))
rown = []
for _ in range(1000):
    rown.append(random_passengers_rownomierny(6))
cn = simulation_cableway(norm)
cr = simulation_cableway(rown)
sn = simulation_ski_lift(norm)
sr = simulation_ski_lift(rown)

print("Polinka rownomierny ", avg_time(cr))
print("Polinka normalny ", avg_time(cn))
print("Wagony rownomierny ", avg_time(sr))
print("Wagony normalny ", avg_time(sn))

print(30*'#')

#czas 5-10
polinka = []
ski = []

q = []
for _ in range(1000):
    q.append(random_passengers_rownomierny(6))
for i in range(6):
    c = simulation_cableway(q, 5+i)
    sl = simulation_ski_lift(q, 5+i)
    polinka.append(avg_time(c))
    ski.append(avg_time(sl))
for i in range(len(polinka)):
    print("Polinka czas ", i+5, ": ", polinka[i])
for i in range(len(ski)):
    print("Wagony czas ", i+5, ": ", ski[i])

print(30*'#')

#miejsca w wagonie
polinka = []
ski = []

q = []
for _ in range(1000):
    q.append(random_passengers_rownomierny(6))
for i in range(4):
    c = simulation_cableway(q)
    sl = simulation_ski_lift(q, miejsca_w_wagonie=i+1)
    polinka.append(avg_time(c))
    ski.append(avg_time(sl))
for i in range(len(polinka)):
    print("Polinka: ", polinka[i])
for i in range(len(ski)):
    print("Wagony ilosc miejsc ", i+1, ": ", ski[i])

print(30*'#')

#miejsca w polince 15 30 45 60
miejsca = [15, 30, 35, 60]
polinka = []
ski = []
q = []
for _ in range(1000):
    q.append(random_passengers_rownomierny(6))
for i in miejsca:
    c = simulation_cableway(q, miejsca_w_polince=i)
    sl = simulation_ski_lift(q)
    polinka.append(avg_time(c))
    ski.append(avg_time(sl))
for i in range(len(polinka)):
    print("Polinka miejsce", miejsca[i], ": ", polinka[i])
for i in range(len(ski)):
    print("Wagony: ", ski[i])

