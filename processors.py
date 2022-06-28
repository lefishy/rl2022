import esper
import components

class RenderProcessor(esper.Processor):
    def __init__(self, console):
        super().__init__()
        self.console = console


    def process(self):
        for ent, (render, pos) in self.world.get_components(components.Renderable, components.Position):
            self.console.print(x=pos.x, y=pos.y, string=render.char)