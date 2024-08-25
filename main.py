from fastapi import FastAPI,Request
from models.TablaSimplex import TablaSimplex
from services.MetodoSimplex import solve_metodo_simplex
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


@app.post("/metodo_simplex")
async def metodo_simplex(tabla:TablaSimplex):
    return solve_metodo_simplex(tabla)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)
