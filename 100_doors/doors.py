class Door:
    def __init__(self, number, is_open):
        self.number = number
        self._is_open = is_open

    @property
    def is_open(self):
        return self._is_open

    def toggle(self):
        self._is_open = not self._is_open


class Row:
    def __init__(self, doors):
        self.doors = []
        for number in range(1, doors + 1):
            self.doors.append(Door(number, False))

    def toggle(self, door):
        self.doors[door - 1].toggle()

    @property
    def opened(self):
        return [door.number for door in self.doors if door.is_open]

    @property
    def closed(self):
        return [door.number for door in self.doors if not door.is_open]

    @property
    def number_of_doors(self):
        return len(self.doors)


class Passer:
    def __init__(self, row):
        self._row = row

    def pass_by(self, toggle_each):
        for door in self._row.doors:
            if door.number % toggle_each == 0:
                door.toggle()

    def make_n_passes(self, n):
        for pass_num in range(1, n + 1):
            self.pass_by(pass_num)

def doors_to_string(door_numbers):
    as_str = [str(door_number) for door_number in door_numbers]
    return ", ".join(as_str)

def main():
    row = Row(doors=100)
    passer = Passer(row)
    passer.make_n_passes(100)
    print("Open Doors: " + doors_to_string(row.opened))

if __name__ == "__main__":
    main()
