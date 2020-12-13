from Klasyprojektu import cableway, ski_lift, passenger, queue
import numpy as np

def random_passengers():
    num = np.random.normal()+3
    if num<=0:
        return 0
    else:
        return int(num)

cable = cableway(50, 10)            # przykadowe cableway
q = queue()                         # pusta kolejka


time = 0
done = False
while not done:
    q.add(random_passengers())      # dodawanie randomowej liczby nowych pasazerow

    cable.move_from_queue(q)        # przenies z kolejki do cableway
    cable.move()
    q.add_time()                    # dodaje wszystkim w kolejce czas oczekiwania

    time +=1
    if time>=1000:                  # zakonczenie symualcji po czasie t = 1000
        done = True

# wyliczanie sredniego czasu czekania
waiting_time=0
for i in cable.people_after:
    waiting_time+=i.waiting_time
print(waiting_time/len(cable.people_after))