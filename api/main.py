from fastapi import APIRouter, FastAPI , HTTPException, status

from fastapi.responses import JSONResponse, RedirectResponse

import random

from pydantic import BaseModel

from ENANOS import FemaleDwarf, MaleDwarf

from custom_exceptions import CustomException, custom_exception_handler

from starlette.exceptions import HTTPException as StarletteHTTPException

class SurnameModel(BaseModel):
    surname: str

def generate_dwarf_surname():
    surnames = ["Ironhammer", "Battleaxe", "Stonehead", "Hardfist", "Bluebeard", "Graymane", "Steelforge", "Shadowstone", "Ironhand", "Longbeard",
                "Ironforge", "Stonebeard", "Goldhammer", "Silvervein", "Thunderaxe", "Darkforge", "Firebeard", "Strongarm", "Bronzebeard", "Ironshield",
                "Battlehammer", "Steelheart", "Rockbreaker", "Mountainborn", "Oakenshield", "Stonewall", "Ironfoot", "Goldbeard", "Fireforge", "Coppervein",
                "Steelbeard", "Stormhammer", "Boulderfist", "Frostbeard", "Ironhelm", "Stoneheart", "Blackforge", "Goldvein", "Emberforge", "Granitejaw",
                "Steelwall", "Ironborn", "Stonefist", "Thunderbeard", "Copperforge", "Steelarm", "Rockshield", "Goldheart", "Firestone", "Ironrock",
                "Silverbeard", "Ironvein", "Stonehelm", "Steelheart", "Goldwall", "Thunderforge", "Emberbeard", "Ironjaw", "Bronzevein", "Steelbeard",
                "Frostforge", "Boulderheart", "Ironfist", "Silverforge", "Stonewall", "Goldborn", "Firebeard", "Ironshield", "Stoneheart", "Copperbeard",
                "Steelvein", "Granitebeard", "Ironwall", "Goldhammer", "Stonearm", "Fireheart", "Ironbeard", "Silverforge", "Stonevein", "Steelhelm",
                "Goldfist", "Fireforge"]
    return random.choice(surnames)

app = FastAPI()

app.include_router(MaleDwarf.router)
app.include_router(FemaleDwarf.router)

app.add_exception_handler(CustomException, custom_exception_handler)
""" app.add_exception_handler(StarletteHTTPException, custom_exception_handler)
app.add_exception_handler(HTTPException, custom_exception_handler)
app.add_exception_handler(Exception, custom_exception_handler) 
 """

@app.get("/cause_error")
async def cause_error():
    # Este endpoint simplemente causa un error para demostrar el manejo de excepciones
    raise HTTPException(status_code=422, detail="Intentional error for demonstration purposes")
@app.get("/generate/dwarf/surname")
async def generate_surname():

    return {"surname": generate_dwarf_surname()}
 
@app.post("/generate/dwarf/surname")
async def post_surname(surname: SurnameModel):
    return {"surname": surname.surname}

