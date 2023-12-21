from queue import Queue
from puzzles.day20.common import Pulse, parse_modules
from utils.read_input import read_input

modules, entry_points = parse_modules(read_input())

button_presses = 1000
pulses_high = 0
pulses_low = button_presses
for i in range(button_presses):
    pulses = Queue[Pulse]()
    for target in entry_points:
        initial = Pulse("broadcaster", target, False)
        pulses.put(initial)
    while not pulses.empty():
        pulse = pulses.get()
        if pulse.high:
            pulses_high += 1
        else:
            pulses_low += 1
        emissions = modules[pulse.target].receive(pulse)
        for emission in emissions:
            pulses.put(emission)

print(pulses_high * pulses_low)
