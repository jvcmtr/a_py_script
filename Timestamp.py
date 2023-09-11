def splitTimestamps(full_string):
    stamp = full_string.split(":")
    obj = {
        "hour": "00",
        "minutes": "00",
        "seconds": "00",
        "frames": "00"
    }

    if len(stamp) == 4:
        obj["hour"] = stamp[0].replace(":","")
        obj["minutes"] = stamp[1].replace(":","")
        obj["seconds"] = stamp[2].replace(":","")
        obj["frames"] = stamp[3].replace(":","")
        return(obj)

    if len(stamp) == 3:
        obj["hour"] = stamp[0].replace(":","")
        obj["minutes"] = stamp[1].replace(":","")
        obj["seconds"] = stamp[2].replace(":","")
        return(obj)

    if len(stamp) == 2:
        obj["minutes"] = stamp[0].replace(":","")
        obj["seconds"] = stamp[1].replace(":","")
        return(obj)



class Timestamp:
    def __init__(self, string):
        stamps = string.split(" - ")

        if len(stamps) < 2 :
            return False
        
        self.begin = splitTimestamps(stamps[0])
        self.end = splitTimestamps(stamps[1])

    def incrementHour(self):
        i = int(self.begin["hour"]) +1
        s = str(i)
        if i<9 :
            s = f"0{i}"
        self.begin["hour"] = s
        
        i = int(self.end["hour"]) +1
        s = str(i)
        if i<9 :
            s = f"0{i}"
        self.end["hour"] = s

    def getString(self):
        return f"{self.begin['hour']}:{self.begin['minutes']}:{self.begin['seconds']}:{self.begin['frames']} - {self.end['hour']}:{self.end['minutes']}:{self.end['seconds']}:{self.end['frames']}"
