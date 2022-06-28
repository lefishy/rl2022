from dataclasses import dataclass as component

@component
class Position:
    x: int = 0
    y: int = 0

@component
class Renderable:
    char: str = ""