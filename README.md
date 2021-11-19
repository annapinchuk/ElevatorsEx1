# SmartElevator


In this task an algorithm is opened for an elevator system of a high-rise building. In general, we will think of a building as having a minimum floor (can be negative) and a maximum floor, when all the intermediate floors exist. Each building will have several elevators (one or more). For simplicity, let's say that each elevator can reach any of the floors. Above all each elevator has characteristics of stopping time, movement start time, and speed (how many floors the elevator passes per second).

In general, we think of the elevators in the building as "smart elevators" meaning: the user simply has to tap the destination floor outside the elevators and then the system has to insert (assign) a particular elevator that is already set to stop at the destination floor.
In this task the challenge will focus on the following optimization challenge:
Given a call to the elevator from the source floor to the destination floor - the system will want to insert the elevator that will minimize the arrival time (arrival time is set to the length of time in seconds between the call to the elevator and between reaching the destination floor). More generally it is said that given a collection of lifts calls on time we would like to define an elevator placement strategy for calls that will minimize the total arrival time for all calls.

### The algorithm

#### Given the total readings is considered the optimal time for them and thus we will assign to each reading a suitable elevator.
#### Given n readings - we would like to coordinate for each elevator from 1 to n readings so that all readings will be performed at the best and most optimal time while combining #### the division between the total elevators in the building.
#### We would like to calculate all the collection options for each elevator that exists in the building, and thus find for each reading the best elevator for it, so that it is #### possible that for some x-elevator there will be a large number of readings.
#### For all associations there are ∑_ (i = 0) ^ n▒ 〖(n¦i)〗 and of each possibility of placing calls to the elevator the total time between all the possibilities of all the #### elevators is calculated similar to the formula from an online ca
#### This problem is similar to the problem of the traveling agent, which has no computational solution in a reasonable time. 


###### Created by Tzach Ofir and Anna 
