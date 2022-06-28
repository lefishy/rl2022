#!/usr/bin/env python3
import tcod
import esper
from  components import Position, Renderable, Movement
from processors import RenderProcessor, MovementProcessor
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    context =  tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Let's try again: 2022 edition",
        vsync=True
    )
    
    root_console = tcod.Console(screen_width, screen_height, order="F")

    world = esper.World()

    render_processor = RenderProcessor(console=root_console)
    movement_processor = MovementProcessor()

    world.add_processor(movement_processor)
    world.add_processor(render_processor)

    player = world.create_entity()

    world.add_component(player, Position(x=1, y=1))
    world.add_component(player, Renderable(char="@"))

    while True:

        world.process()

        context.present(root_console)

        for event in tcod.event.wait():
            action = event_handler.dispatch(event)

            if action is None:
                continue

            if isinstance(action, MovementAction):
                world.add_component(player, Movement(action.dx, action.dy))

            elif isinstance(action, EscapeAction):
                raise SystemExit()



if __name__ == "__main__":
    main()