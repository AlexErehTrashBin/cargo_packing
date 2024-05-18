class Truck(object):
    def __init__(self, capacity):
        self.initial_capacity = capacity
        self.remaining_capacity = capacity
        self.items = []

    def __str__(self):
        return f"Truck(Rem Cap: {self.remaining_capacity}, Items: {self.items})"

    def __repr__(self):
        return f"Truck(Rem Cap: {self.remaining_capacity}, Items: {self.items})"

    def __hash__(self):
        return hash(self.remaining_capacity)

    def print_items(self):
        for item in self.items:
            print(item)

    def add_cargo(self, item):
        self.items.append(item)
        self.remaining_capacity -= item.size

    def remove_item(self, item):
        self.items.remove(item)
        self.remaining_capacity += item.size

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        if self.remaining_capacity != other.remaining_capacity:
            return False
        if len(self.items) != len(other.items):
            return False
        return True


class Cargo(object):
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"C({self.size})"

    def __repr__(self):
        return f"C({self.size})"

    def __eq__(self, other):
        return self.size == other.size

    def __lt__(self, other):
        return self.size < other.size
