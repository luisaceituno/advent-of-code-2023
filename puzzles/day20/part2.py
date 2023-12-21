from itertools import count
from math import lcm, prod
from queue import Queue
from puzzles.day20.common import Pulse, parse_modules
from utils.read_input import read_input


modules, entry_points = parse_modules(read_input())

button_pressed = 0
gate = next(module for module in modules.values() if "rx" in module.targets)
logs: dict[str, list[int]] = {}
for press_count in count():
    pulses = Queue[Pulse]()
    for target in entry_points:
        initial = Pulse("broadcaster", target, False)
        pulses.put(initial)
    while not pulses.empty():
        pulse = pulses.get()
        emissions = modules[pulse.target].receive(pulse)
        for emission in emissions:
            pulses.put(emission)
        if pulse.target == gate.name and pulse.high:
            logs.setdefault(pulse.sender, [])
            logs[pulse.sender].append(press_count)
    if logs and all(len(l) > 1 for l in logs.values()):
        break

print(lcm(*(l[1] - l[0] for l in logs.values())))
