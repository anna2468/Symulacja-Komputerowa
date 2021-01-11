from Klasyprojektu import cableway, ski_lift, passenger, queue, carriage
import numpy as np

def random_passengers_rownomierny(n=5):
    num = np.random.randint(n+1)
    return int(num)

def random_passengers_normal(n=5):
    num = np.random.normal()+n
    if int(num)>=0:
        return int(num)
    else:
        return 0

def simulation_cableway(new_passengers_list, miejsca_w_polince=60):
    cable = cableway(miejsca_w_polince, 10)
    q = queue([])
    for i in new_passengers_list:
        q.add(i)
        cable.move_from_queue(q)
        cable.move()
        q.add_time()
    return cable.people_after

def simulation_ski_lift(new_passengers_list, miejsca_w_wagonie=5):
    ski = ski_lift(miejsca_w_wagonie, 10, 1)
    q= queue([])
    for i in new_passengers_list:
        q.add(i)

        ski.move_from_queue(q)
        ski.move()

        q.add_time()
    return ski.get_people_out()

def avg_time(x):
    waiting_time = 0
    l = len(x)
    for i in x:
        waiting_time += i.waiting_time
    x = []
    return waiting_time/l

result = []

#polinka uni
miejsca_p = [15, 30, 45, 60]
czasy = []
for m in miejsca_p:
    czas = []
    for _ in range(50):
        qu = []
        for _ in range(100):
            qu.append(random_passengers_rownomierny())
        s = simulation_cableway(qu, m)
        czas.append(avg_time(s))
    czasy.append(czas)

for i in range(len(czasy)):
    for j in range(len(czasy[i])):
        result.append(["Polinka rozklad: rownomierny, miejsca:"+ str(miejsca_p[i]),czasy[i][j]])
        print("Polinka rozklad: rownomierny, miejsca:", miejsca_p[i], ", czas:", czasy[i][j])

#polinka nor
miejsca_p = [15, 30, 45, 60]
czasy = []
for m in miejsca_p:
    czas = []
    for i in range(50):
        q = []
        for _ in range(100):
            q.append(random_passengers_normal())
        czas.append(avg_time(simulation_cableway(q, m)))
    czasy.append(czas)

for i in range(len(czasy)):
    for j in range(len(czasy[i])):
        result.append(["Polinka rozklad: normalny, miejsca:"+ str(miejsca_p[i]),czasy[i][j]])
        print("Polinka rozklad: normalny, miejsca:", miejsca_p[i], ", czas:", czasy[i][j])

#wyciag uni
miejsca_p = [1, 2, 3, 4]
czasy = []
for m in miejsca_p:
    czas = []
    for _ in range(50):
        q = []
        for _ in range(100):
            q.append(random_passengers_rownomierny())
        czas.append(avg_time(simulation_ski_lift(q, m)))
    czasy.append(czas)

for i in range(len(czasy)):
    for j in range(len(czasy[i])):
        result.append(["Wyciag rozklad: rownomierny, miejsca:"+ str(miejsca_p[i]),czasy[i][j]])
        print("Wyciag rozklad: rownomierny, miejsca:", miejsca_p[i], ", czas:", czasy[i][j])

#wyciag nor
#wyciag uni
miejsca_p = [1, 2, 3, 4]
czasy = []
for m in miejsca_p:
    czas = []
    for _ in range(50):
        q = []
        for _ in range(100):
            q.append(random_passengers_normal())
        czas.append(avg_time(simulation_ski_lift(q, m)))
    czasy.append(czas)

for i in range(len(czasy)):
    for j in range(len(czasy[i])):
        result.append(["Wyciag rozklad: normalny, miejsca:"+ str(miejsca_p[i]),czasy[i][j]])
        print("Wyciag rozklad: normalny, miejsca:", miejsca_p[i], ", czas:", czasy[i][j])

np.savetxt('result.csv', result, delimiter=", ", fmt='% s')