import esper
from components import Position, Movement, Renderable

class RenderProcessor(esper.Processor):
    def __init__(self, console):
        super().__init__()
        self.console = console


    def process(self):
        self.console.clear()

        for ent, (render, pos) in self.world.get_components(Renderable, Position):
            self.console.print(x=pos.x, y=pos.y, string=render.char)

class MovementProcessor(esper.Processor):

    def process(self):
        for ent, (mov, pos) in self.world.get_components(Movement, Position):
            pos.x += mov.dx
            pos.y += mov.dy
            self.world.remove_component(ent, Movement)