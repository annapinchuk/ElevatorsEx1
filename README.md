## Schedule Elevators - Ex1 - OOP

### Defining The Problem
Write an OOP 'Elevator project' using an Algorithm based on the concept of "Smart Elevator". 

The assignment is to build an offline algorithm matching a call for an elevator.
The Algorithm is going to consider all the buildings,elevators and elevator calls which are already given to us and make the perfect match by calculating the most efficient and optimal route.

## References
* Description of the Designated Dispatch algorithm method on [Elevatorpedia](https://elevation.fandom.com/wiki/Destination_dispatch) website which explains an optimization technique used to group passengers with the same destination to the same single lifts,by doing that the algorithm will reduce wait time by eliminating unnecessary stops.

* The study : [Decision-Theoretic Group Elevator Scheduling](https://www.aaai.org/Papers/ICAPS/2003/ICAPS03-014.pdf),explains an algorithm that optimizes matching the calls to the elevator using Dynamic Programing.

* the study :[Elevator Control Using Reinforcement Learning
to Select Strategy](https://www.kth.se/social/files/588617c2f276547fe1dbf8d2/AJanssonKUgglaLingvall_dkand15.pdf), Focuses on finding the optimal solution for matching a call to an elevator issue by using AI programing which selects the best algorithm out of 5 , depending on a specific case.



## Code Design - classes
### elevator 
Represents an elevator in the building.<br/>
#### each elevator has:
* speed <br/>
* min_floor<br/>
* max_floor <br/>
* close_time<br/>
* open_time<br/>
* start_time <br/>
* stop_time<br/>
### building
Represents a building.<br/>
#### each building has:
* min_floor<br/>
* max_floor <br/>
* elevators (the exact number of elevators in this building)<br/>
### callforelevator
Represents the call allcated to the elevator.
#### each call has:
* time<br/>
* src <br/>
* dest <br/>
* state <br/>
* elev (the specific elevator that takes the call)<br/>
### main
This class contains the main functions.
#### main: 
Creating new elemenrs to run, and use all the function below to run the algorithm
#### allocate_call_for_elev:
Matches a call for specific elevator using the devition algorithm.
#### j_to_building: 
Take the given JSONs and converting them into a building.
#### csv_to_calls: 
Take the given CSV file and converting it into calls.
#### csv_output_writer: 
Take the reusalts of the algorithm and write it into output file.
### elev_test_main
Testing the main algorithm function : 
```sh 
allocate_call_for_elev
```

## Log files

## UML Diagram
