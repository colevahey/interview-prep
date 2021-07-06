On an infinite plane, a robot initially stands at `(0, 0)`
and faces north. The robot can receive one of three
instructions:  
 - `"G"`: go straight 1 unit  
 - `"L"`: turn 90 degrees to the left  
 - `"R"`: turn 90 degrees to the right  

The robot performs the `instructions` given in order, and
repeats them forever.

Return `true` if and only if there exists a circle in the
plane such that the robot never leaves the circle.

### Solution Input
```Python3
instructions = "GGLLGG"
```
 
### Solution Output
```Python3
True
# The robot moves to (0, 2) and then returns to (0, 0)
# The next time, the robot moves to (0, -2) and then back
# to the origin, and remains in this circle forever
```
