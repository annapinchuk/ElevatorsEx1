class callforelevator:

    def __init__(self,time, src, dest, state, elev):
        self.time = time
        self.src = int(src)
        self.dest = int(dest)
        self.state = state
        self.elev = elev


    def __str__(self):
        return ", ".join([
            str(self.time),
            str(self.src),
            str(self.dest),
            str(self.state),
            str(self.elev)])

    def for_out(self):
        return "Elevator call", self.time, str(self.src), str(self.dest), 0, str(self.elev)
