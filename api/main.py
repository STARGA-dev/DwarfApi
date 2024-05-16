from fastapi import APIRouter, FastAPI
import random
from pydantic import BaseModel
from ENANOS import FemaleDwarf, MaleDwarf

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

@app.get("/generate/dwarf/surname")
async def generate_surname():
    return {"surname": generate_dwarf_surname()}
@app.post("/generate/dwarf/surname")
async def post_surname(surname: SurnameModel):
    return {"surname": surname.surname}