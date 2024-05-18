from typing import List, Tuple

from models import Truck, Cargo


def state_hash(cargos: List[Cargo], trucks: List[Truck]) -> str:
    """
    Возвращает строку отвечающее за состояние списков грузов и грузовиков.
    :param cargos:
    :type cargos:
    :param trucks:
    :type trucks:
    :return:
    :rtype:
    """

    s: str = hex(len(cargos))[2:]
    for truck in trucks:
        s: str = s + hex(truck.remaining_capacity)[2:] + " "
    return s


def dynamic_branch_and_bound(cargos: List[Cargo], best_solution: List[Truck], initial_capacity: int) -> List[Truck]:
    cargos.sort()
    stack: List[Tuple[List[Cargo], List[Truck]]] = [(cargos, [])]
    visited: List[str] = []
    while len(stack) > 0:

        na = stack.pop()
        cargos, trucks = na

        if len(trucks) >= len(best_solution):
            continue

        if (state_hash(cargos, trucks)) in visited:
            continue
        visited.append(state_hash(cargos, trucks))

        if len(cargos) == 0:
            if len(trucks) < len(best_solution):
                best_solution = trucks
            continue

        visited.append(state_hash(cargos, trucks))
        cargo = cargos[0]

        new_trucks = trucks.copy()
        new_truck = Truck(initial_capacity)
        new_truck.add_cargo(cargo)
        new_trucks.append(new_truck)
        new_cargos = cargos.copy()
        new_cargos.remove(cargo)
        stack.append((new_cargos, new_trucks))

        for truck in trucks:
            if truck.remaining_capacity >= cargo.size:
                new_trucks = trucks.copy()
                new_trucks.remove(truck)
                new_truck = Truck(truck.initial_capacity)
                new_truck.remaining_capacity = truck.remaining_capacity
                new_truck.items = truck.items.copy()
                new_truck.add_cargo(cargo)
                new_trucks.append(new_truck)
                new_cargos = cargos.copy()
                new_cargos.remove(cargo)
                stack.append((new_cargos, new_trucks))

    return best_solution


def first_fit(cargos, initial_capacity, trucks) -> List[Truck]:
    if trucks is None:
        trucks: List[Truck] = []
    for cargo in cargos:
        for truck in trucks:
            if truck.remaining_capacity >= cargo.size:
                truck.add_cargo(cargo)
                break
        else:
            truck: Truck = Truck(initial_capacity)
            truck.add_cargo(cargo)
            trucks.append(truck)
    return trucks


if __name__ == '__main__':
    # Вместимость каждого грузовика
    truck_capacity: int = 100
    # Веса грузов
    cargo_weights: List[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    items: List[Cargo] = list(map(lambda x: Cargo(x), cargo_weights))
    nb_items: int = len(items)
    cargos_ff: List[Truck] = first_fit(items, truck_capacity, None)
    cargos_bb: List[Truck] = dynamic_branch_and_bound(items, cargos_ff, truck_capacity)
    for truck in enumerate(cargos_bb):
        print(truck[1])
