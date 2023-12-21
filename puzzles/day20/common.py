from dataclasses import dataclass

from utils.read_input import read_input


@dataclass
class Pulse:
    sender: str
    target: str
    high: bool


@dataclass
class FlipFlop:
    name: str
    targets: list[str]
    on: bool = False

    def add_src(self, src: str):
        pass

    def receive(self, pulse: Pulse) -> list[Pulse]:
        if not pulse.high:
            self.on = not self.on
            return [Pulse(self.name, target, self.on) for target in self.targets]
        return []


@dataclass
class Conjunction:
    name: str
    targets: list[str]
    memory: dict[str, bool] = None

    def __post_init__(self):
        self.memory = {}

    def add_src(self, src: str):
        self.memory[src] = False

    def receive(self, pulse: Pulse) -> list[Pulse]:
        self.memory[pulse.sender] = pulse.high
        high = not all(self.memory.values())
        return [Pulse(self.name, target, high) for target in self.targets]


def parse_modules(input: list[str]):
    modules: dict[str, FlipFlop | Conjunction] = {}
    entry_points: list[str] = []
    for line in input:
        src, *targets = line.replace("->", "").replace(",", "").split()
        if src == "broadcaster":
            entry_points.extend(targets)
        elif src[0] == "%":
            module = FlipFlop(src[1:], targets)
            modules[module.name] = module
        elif src[0] == "&":
            module = Conjunction(src[1:], targets)
            modules[module.name] = module

    dummys = []
    for module in modules.values():
        for target in module.targets:
            if target in modules:
                modules[target].add_src(module.name)
            else:
                dummys.append(target)

    for dummy in dummys:
        modules[dummy] = FlipFlop("", [])

    return modules, entry_points
