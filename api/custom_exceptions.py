from fastapi import Request,  HTTPException, status, APIRouter
from fastapi.responses import JSONResponse, RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request

class CustomException(Exception):
    def __init__(self, name: str, status_code: int):
        self.name = name
        self.status_code = status_code

async def custom_exception_handler(request: Request, exc: CustomException):
    
    valid_status_codes = [
        100, 101, 102, 200, 201, 202, 203, 204, 206, 207, 300, 301, 302, 303, 304,
        305, 307, 308, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412,
        413, 414, 415, 416, 417, 418, 420, 421, 422, 423, 424, 425, 426, 429, 431,
        444, 450, 451, 499, 500, 501, 502, 503, 504, 506, 507, 508, 509, 510, 511,
        599
    ]
    
    

    
    return RedirectResponse(url=f"https://http.cat/{exc.status_code}")


