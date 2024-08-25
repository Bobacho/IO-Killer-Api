from pydantic import BaseModel

class TablaSimplex(BaseModel):
    matriz: list[list[float]]
    restricciones: list[float]
    objetivo: list[float]
    basic: list[int]
