#!/usr/bin/env python3
import tcod
import esper
import components
import processors

def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    context =  tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Let's try again: 2022 edition",
        vsync=True
    )
    
    root_console = tcod.Console(screen_width, screen_height, order="F")

    world = esper.World()

    render_processor = processors.RenderProcessor(console=root_console)

    world.add_processor(render_processor)

    player = world.create_entity()

    world.add_component(player, components.Position(x=1, y=1))
    world.add_component(player, components.Renderable(char="@"))

    while True:
        world.process()

        context.present(root_console)

        for event in tcod.event.wait():
            if event.type == "QUIT":
                raise SystemExit()



if __name__ == "__main__":
    main()