from pydantic import BaseModel
from fastapi import APIRouter , FastAPI
import random
class NameModel(BaseModel):
    name: str
def generate_male_dwarf_name():
   name = ["Thordin","Balin","Durgin","Hrothgar","Hrothgar","Kragar","Thorgrim","Borin","Grumir","Thrain","Korgin","Durak","Thrym","Gormir","Hjorin","Throvar","Dagrim","Throrin",
        "Grungar","Thralin","Brunir","Grorim","Thorak","Thrandar","Vornir","Brudar","Thrynn","Drorin","Grilin","Thormar","Burin","Grunur","Throgar","Kaldur","Brurin","Grumbar",
        "Thralgrom","Throgrim","Thorburin","Thrainar","Kolbiro","Thrynnorin","Thragrim","Grumur","Throrok","Grumlin","Throvalin","Grindar","Thrymborin","Grumirin","Thordak","Thorgrimin","Thrymburin","Throrim",
        "Thorric","Brorn","Dargrim","Thurgar","Thralinor","Grorin","Grunak","Thormin","Throldir","Bramir","Throric","Thrainor","Throrund","Thrymgar","Thordir","Thromak","Grorik","Thromir",
        "Grudin","Thrainak","Thrombar","Brugin","Thromlin","Grunar","Thrimak","Throrimak","Drolin","Thralmuk","Thrainir","Thrylgar","Thronak","Grondar","Throrum","Thrainar","Thorgar","Thrumir",
        "Brudak","Thrandak","Thormir","Thragak","Thralnak","Thragar","Thromlok","Thrumlok","Thorglok","Thralglok",]

   return random.choice(name) 
router = APIRouter()     
@router.get("/generate/dwarf/male/")
async def generate_name():
    return {"name": generate_male_dwarf_name()} 
@router.post("/generate/dwarf/male/")
async def post_name(name: NameModel):
    return {"name": name.name}