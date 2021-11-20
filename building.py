class building:
    def __init__(self, elevators, min_floor, max_floor):
        self.elevators = elevators
        self.min_floor = min_floor
        self.max_floor = max_floor

    def sort_speed_elev(self, call):
        self.elevators = sorted(
            self.elevators,
            key=lambda y:
            y.StartTime +
            y.StopTime +
            y.CloseTime +
            y.OpenTime -
            abs(call.dest - call.src / y.Speed))

    def __str__(self):

        elevator_str = ','.join("{ " + str(e) + " }" for e in self.elevators)

        return ",".join([
            str(self.min_floor),
            str(self.max_floor),
            "".join(["[", ", ".join(["".join(['{', str(x), '}']) for x in self.elevators]), "]"])])