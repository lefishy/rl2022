from dataclasses import dataclass as component

@component
class Position:
    x: int = 0
    y: int = 0

@component
class Movement:
    dx: int = 0
    dy: int = 0

@component
class Renderable:
    char: str = ""