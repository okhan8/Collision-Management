import threading
import time
import sys
from time import sleep
from random import randint


qASem = threading.Semaphore()
qBSem = threading.Semaphore()

#position of x and y and z in different buffers
x_coordinates = {'x': randint(0,6), 'y': randint(0,7), 'failure': randint(0,1), "movement": 'X'} #fault of value 1 means the train cannot be stopped
movementX = randint(0,2);
if movementX is 0:
    x_coordinates['movement']= 'XY';
elif movementX is 1:
    x_coordinates['movement']= 'X'
else:
    x_coordinates['movement']= 'Y'

x_F = {'x': 0, 'y': 0} #The future position of object X

y_coordinates = {'x': randint(0,6), 'y': randint(0,7), 'failure': randint(0,9), "movement": 'Y'}
movementY = randint(0,2);
if movementY is 0:
    y_coordinates['movement']= 'XY';
elif movementY is 1:
    y_coordinates['movement']= 'X'
else:
    y_coordinates['movement']= 'Y'
y_F = {'x':1, 'y':1}

z_coordinates = {'x': randint(0,6), 'y': randint(0,7), 'failure': randint(0,99), "movement": 'XY'}
movementZ = randint(0,2);
if movementZ is 0:
    z_coordinates['movement']= 'XY';
elif movementZ is 1:
    z_coordinates['movement']= 'X'
else:
    z_coordinates['movement']= 'Y'
z_F = {'x':2, 'y':2}

t=0;


print("X starting position is ("+x_coordinates['x'].__str__()+","+x_coordinates['y'].__str__()+")")
print("X is moving in "+x_coordinates['movement']+" direction")

print("Y starting position is ("+y_coordinates['x'].__str__()+","+y_coordinates['y'].__str__()+")")
print("Y is moving in "+y_coordinates['movement']+" direction")

print("Z starting position is ("+z_coordinates['x'].__str__()+","+z_coordinates['y'].__str__()+")")
print("Z is moving in "+z_coordinates['movement']+" direction")




def collsion():
    t=0;
    while t<20:
        t=t+1
        qASem.acquire()
        if x_coordinates["x"] is (y_coordinates["x"]) and x_coordinates["y"] is (y_coordinates["y"]):
            print("A collision has occured between x and y at coordinates (" + x_coordinates["x"].__str__()+","+x_coordinates["y"].__str__()+",")
            t=20


        if x_coordinates["x"] is (z_coordinates["x"]) and x_coordinates["y"] is (z_coordinates["y"]):
            print("A collision has occured between x and z at coordinates (" + x_coordinates["x"].__str__() + "," + x_coordinates["y"].__str__() + ") and z is ("+ z_coordinates['x'].__str__()+","+z_coordinates['y'].__str__()+",")
            t=20

        if y_coordinates["x"]is (z_coordinates["x"]) and y_coordinates["y"]is (z_coordinates["y"]):
            print("A collision has occured between y and z at coordinates (" + y_coordinates["x"].__str__() + "," + y_coordinates["y"].__str__()+")")
            t=20

        print("Train x coordinates is ("+x_coordinates['x'].__str__()+","+x_coordinates["y"].__str__()+")"+ " y is ("+ y_coordinates['x'].__str__()+","+y_coordinates['y'].__str__()+") z is ("+z_coordinates['x'].__str__()+","+z_coordinates['y'].__str__()+")")
        #print ("Fault for X Y Z value is: ("+ x_coordinates['failure'].__str__() +","+ y_coordinates['failure'].__str__()+ "," + z_coordinates['failure'].__str__()+")");

        qASem.release()
        sleep(1.0)

def updateX():
    if x_coordinates['movement'] is 'XY':
        if x_coordinates['x'] is 6:
            x_coordinates['x'] = 0
            x_F['x'] = x_coordinates['x']+1
        else:
            x_coordinates['x'] = x_coordinates['x'] + 1;
            if x_coordinates['x'] is 6:
                x_F['x'] = 0
            else:
                x_F['x'] = x_coordinates['x'] + 1
        if x_coordinates['y'] is 7:
            x_coordinates['y'] = 0;
            x_F['y'] = x_coordinates['y'] + 1
        else:
            x_coordinates['y'] = x_coordinates['y'] + 1;
            if x_coordinates['y'] is 7:
                x_F['y'] = 0;
            else:
                x_F['y'] = x_coordinates['y'] + 1

    if x_coordinates['movement'] is 'X':
        x_F['y'] = x_coordinates['y']
        if x_coordinates['x'] is 6:
            x_coordinates['x'] = 0
            x_F['x'] = x_coordinates['x'] + 1
        else:
            x_coordinates['x'] = x_coordinates['x'] + 1;
            if x_coordinates['x'] is 6:
                x_F['x'] = 0;

            else:
                x_F['x'] = x_coordinates['x'] + 1

    if x_coordinates['movement'] is 'Y':
        x_F['x'] = x_coordinates['x']
        if x_coordinates['y'] is 7:
            x_coordinates['y'] = 0;
            x_F['y'] = x_coordinates['y'] + 1
        else:
            x_coordinates['y'] = x_coordinates['y'] + 1;
            if x_coordinates['y'] is 7:
                x_F['y'] = 0;
            else:
                x_F['y'] = x_coordinates['y'] + 1


def updateY():
    if y_coordinates['movement'] is 'XY':
        if y_coordinates['x'] is 6:
            y_coordinates['x'] = 0
            y_F['x'] = y_coordinates['x'] + 1
        else:
            y_coordinates['x'] = y_coordinates['x'] + 1;
            if y_coordinates['x'] is 6:
                y_F['x'] = 0

            else:
                y_F['x'] = y_coordinates['x'] + 1

        if y_coordinates['y'] is 7:
            y_coordinates['y'] = 0;
            y_F['y'] = y_coordinates['y'] + 1

        else:
            y_coordinates['y'] = y_coordinates['y'] + 1;
            if y_coordinates['y'] is 7:
                y_F['y'] = 0;
            else:
                y_F['y'] = y_coordinates['y'] + 1

    if y_coordinates['movement'] is 'X':
        y_F['y'] = y_coordinates['y']
        if y_coordinates['x'] is 6:
            y_coordinates['x'] = 0
            y_F['x'] = y_coordinates['x'] + 1
        else:
            y_coordinates['x'] = y_coordinates['x'] + 1;
            if y_coordinates['x'] is 6:
                y_F['x'] = 0;
            else:
                y_F['x'] = y_coordinates['x'] + 1

    if y_coordinates['movement'] is 'Y':
        y_F['x'] = y_coordinates['x']
        if y_coordinates['y'] is 7:
            y_coordinates['y'] = 0;
            y_F['y'] = y_coordinates['y'] + 1
        else:
            y_coordinates['y'] = y_coordinates['y'] + 1;
            if y_coordinates['y'] is 7:
                y_F['y'] = 0;
            else:
                y_F['y'] = y_coordinates['y'] + 1

def updateZ():
    if z_coordinates['movement'] is 'XY':
        if z_coordinates['x'] is 5:
            z_coordinates['x'] = 0
            z_F['x'] = z_coordinates['x'] + 2
        elif z_coordinates['x'] is 6:
            z_coordinates['x'] = 1
            z_F['x'] = z_coordinates['x'] + 2
        else:
            z_coordinates['x'] = z_coordinates['x'] + 2;
            if z_coordinates['x'] is 5:
                z_F['x'] = 0;
            elif z_coordinates['x'] is 6:
                z_F['x'] = 1;
            else:
                z_F['x'] = z_coordinates['x'] + 2

        if z_coordinates['y'] is 6:
            z_coordinates['y'] = 0;
            z_F['y'] = z_coordinates['y'] + 2

        elif z_coordinates['y'] is 7:
            z_coordinates['y'] = 1;
            z_F['y'] = z_coordinates['y'] + 2
        else:
            z_coordinates['y'] = z_coordinates['y'] + 2;
            if z_coordinates['y'] is 6:
                z_F['y'] = 0;
            elif z_coordinates['y'] is 7:
                z_F['y'] = 1;
            else:
                z_F['y'] = z_coordinates['y'] + 2


    if z_coordinates['movement'] is 'X':
        z_F['y'] = z_coordinates['y']
        if z_coordinates['x'] is 5:
            z_coordinates['x'] = 0
            z_F['x'] = z_coordinates['x'] + 2

        elif z_coordinates['x'] is 6:
            z_coordinates['x'] = 1;
            z_F['x'] = z_coordinates['x'] + 2

        else:
            z_coordinates['x'] = z_coordinates['x'] + 2;
            if z_coordinates['x'] is 5:
                z_F['x'] = 0;
            elif z_coordinates['x'] is 6:
                z_F['x'] = 1;
            else:
                z_F['x'] = z_coordinates['x'] + 2

    if z_coordinates['movement'] is 'Y':
        z_F['x'] = z_coordinates['x'];
        if z_coordinates['y'] is 6:
            z_coordinates['y'] = 0;
            z_F['y'] = z_coordinates['y'] + 2
        elif z_coordinates['y'] is 7:
            z_coordinates['y'] = 1;
            z_F['y'] = z_coordinates['y'] + 2

        else:
            z_coordinates['y'] = z_coordinates['y'] + 2;
            if z_coordinates['y'] is 6:
                z_F['y'] = 0;
            elif z_coordinates['y'] is 7:
                z_F['y']= 1;
            else:
                z_F['y'] = z_coordinates['y'] + 2


def update():
    t=0;
    while t<20:
        t= t+1;
        qBSem.acquire()
        y_coordinates['failure'] = randint(0, 9);
        z_coordinates['failure'] = randint(0, 99);
        x_coordinates['failure'] = randint(0, 1);
        #print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
            #'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");
        if x_F['x'] is y_F['x'] and x_F['y'] is y_F['y'] and x_F['x'] is z_F['x'] and x_F['y'] is z_F['y']:
            if z_coordinates['failure'] is not 1 and y_coordinates['failure'] is not 1:
                updateX()
                print("3 way collision avoided by stopping y and z");
                print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                    'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");

            elif x_coordinates['failure'] is not 1 and y_coordinates['failure'] is not 1:
                print ("Fault in z")
                updateZ()
                print("3 way collision avoided by stopping x and y")
                print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                    'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");

            elif x_coordinates['failure'] is not 1 and z_coordinates['failure'] is not 1:
                print ('Fault in y')
                updateY()
                print("3 way collision avoided by stopping x and z")
                print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                    'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");

            else:
                if z_coordinates['failure'] is 1:
                    print("Fault in z");
                if y_coordinates('failure') is 1:
                    print("Fault in y")
                if x_coordinates['failure'] is 1:
                    print ("Fault in x")
                print ("3 way collision could not be avoided because of faults detected")
                print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                    'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");
                t=20
        else:
            if x_F['x']  is y_F['x'] and x_F['y'] is y_F['y']:
                if (x_coordinates['failure'] is 1 and y_coordinates['failure'] is not 1) and (y_coordinates['x'] is not z_F['x'] \
                        or y_coordinates['y'] is not z_F['y']):
                    print ("fault detected in train x, cannnot stop it");
                    updateX();
                    updateZ()
                    print ("Stopped train y and x moved");
                    print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                        'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");

                elif (y_coordinates['failure'] is 1 and x_coordinates['failure'] is not 1) and (x_coordinates['x'] is not z_F['x'] \
                        or x_coordinates['y'] is not z_F['y']):
                        print("fault detected in train y, cannot stop it");
                        updateY()
                        updateZ()
                        print("Stopped train x and y moved");
                        print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                            'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");
                elif (x_coordinates['failure'] is not 1 and y_coordinates['failure'] is not 1) and (y_coordinates['x'] is not z_F['x'] \
                        or y_coordinates['y'] is not z_F['y']):
                    updateX();
                    updateZ()
                    print("Stopped train y and x moved");
                    print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                        'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");
                elif (y_coordinates['failure'] is not 1 and x_coordinates['failure'] is not 1) and (x_coordinates['x'] is not\
                        z_F['x'] or x_coordinates['y'] is not z_F['y']):
                    updateY()
                    updateZ()
                    print("Stopped train x and y moved");
                    print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                        'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");

                else:
                    updateX();
                    updateY();
                    updateZ();
                    print("Both trains x and y cannot be stopped, unavoidable collison ");
                    t=20


            elif x_F['x'] is z_F['x'] and x_F['y'] is z_F['y']:
                if (x_coordinates['failure'] is 1 and z_coordinates['failure'] is not 1) and (z_coordinates['x'] is not y_F['x'] \
                        or z_coordinates['y'] is not y_F['y']):
                    print("fault detected in train x, cannnot stop it");
                    updateX();
                    updateY()
                    print("Stopped train z and x moved")
                    print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                        'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");
                elif (z_coordinates['failure'] is 1 and x_coordinates['failure'] is not 1) and (x_coordinates['x'] is not y_F['x'] \
                        or x_coordinates['y'] is not y_F['y']):
                    print("fault detected in train z, cannot stop it");
                    updateZ()
                    updateY()
                    print("Stopped train x and z moved");
                    print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                        'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");
                elif (x_coordinates['failure'] is not 1 and z_coordinates['failure'] is not 1) and (z_coordinates['x'] is not y_F['x'] \
                        or z_coordinates['y'] is not y_F['y']):
                    updateX();
                    updateY()
                    print("Stopped train z and x moved")
                    print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                        'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");
                elif (z_coordinates['failure'] is not 1 and x_coordinates['failure'] is not 1) and (x_coordinates['x'] is not y_F['x'] \
                        or x_coordinates['y'] is not y_F['y']):
                    updateZ()
                    updateY()
                    print("Stopped train x and z moved");
                    print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                        'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");
                else:
                    updateX();
                    updateY();
                    updateZ();
                    print("Both trains x and z cannot be stopped, unavoidable collison");
                    print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                        'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");
                    t=20


            elif y_F['x'] is z_F['x'] and y_F['y'] is z_F['y']:
                if (z_coordinates['failure'] is not 1 and y_coordinates['failure'] is 1)\
                        and (z_coordinates['x'] is not x_F['x'] or z_coordinates['y'] is not x_F['y']):
                    print ("fault detected in train y, cannot stop it")
                    updateY()
                    updateX()
                    print ("stopped train z and y moved")
                    print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                        'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");
                elif (y_coordinates['failure'] is not 1 and z_coordinates['failure'] is 1)\
                        and (y_coordinates['x'] is not x_F['x'] or y_coordinates['y'] is not x_F['y']):
                    print ("fault detect in train z, cannot stop it")
                    updateZ()
                    updateX()
                    print("Stopped train Y and z moved")
                    print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                        'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");
                elif (z_coordinates['failure'] is not 1 and y_coordinates['failure'] is not 1)\
                        and (z_coordinates['x'] is not x_F['x'] or z_coordinates['y'] is not x_F['y']):
                    updateY()
                    updateX()
                    print("stopped train z and y moved")
                    print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                        'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");
                elif (z_coordinates['failure'] is not 1 and y_coordinates['failure'] is not 1)\
                        and (y_coordinates['x'] is not x_F['x'] or y_coordinates['y'] is not x_F['y']):
                    updateZ()
                    updateX()
                    print("stopped train y and z moved")
                    print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                        'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");
                else:
                    updateX();
                    updateY();
                    updateZ();
                    print ("Could not stop train y or z due to fault, collision unavoidable")
                    print("Fault for X Y Z value is: (" + x_coordinates['failure'].__str__() + "," + y_coordinates[
                        'failure'].__str__() + "," + z_coordinates['failure'].__str__() + ")");
                    t=20
            else:
                updateX()
                updateY()
                updateZ()

        qBSem.release()
        sleep(1.04)


t1 = threading.Thread(target=collsion);
t2 = threading.Thread(target=update);


t1.start()
t2.start()

t1.join()
t2.join()



