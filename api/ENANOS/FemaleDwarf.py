from pydantic import BaseModel
from fastapi import APIRouter , FastAPI
import random


def generate_female_dwarf_name():
    name = ["Brunilda","Thora","Dorna","Gwendolyn","Balina","Durina","Thraina","Brynhild","Freydis","Helga",
"Thyri","Solveig","Thyra","Gerda","Ragnhild","Ingrid","Sigrid","Astrid","Hilda","Elinor",
"Freya","Sif","Ragnild","Svanhild","Borgny","Thora","Sigrun","Sigga","Gunnhild","Hervor",
"Borghild","Thora","Drifa","Gunvor","Idunn","Estrid","Oddny","Gudrun","Ingeborg","Brynja",
"Estrid","Solvej","Ylva","Sigurlina","Hjordis","Vigdis","Helka","Ragna","Ingunn","Thordis",
"Aldis","Jorunn","Tora","Sigrunn","Solveig","Gunnvor","Inga","Halldora","Arnbjorg","Rannveig",
"Yngvild","Audhild","Asdis","Thordis","Solveig","Ragna","Estrid","Eir","Gudrid","Dagny",
"Groa","Runa","Svanhild","Bryndis",
]
    return random.choice(name)
router = APIRouter()    
@router.get("/generate/dwarf/female")
async def generate_name2():
    return {"name": generate_female_dwarf_name()} 
