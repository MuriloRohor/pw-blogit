from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
def get_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    
@app.get('/usuario/login', response_class=HTMLResponse)
def get_main(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get('/usuario/novo', response_class=HTMLResponse)
def get_main(request: Request):
    return templates.TemplateResponse("criarconta.html", {"request": request})

@app.get('/contato', response_class=HTMLResponse)
def get_termos(request: Request):
    return templates.TemplateResponse("contato.html", {"request": request})

@app.get('/termos', response_class=HTMLResponse)
def get_termos(request: Request):
    return templates.TemplateResponse("termos.html", {"request": request})

@app.get('/alterar', response_class=HTMLResponse)
def get_termos(request: Request):
    return templates.TemplateResponse("termos.html", {"request": request})


@app.get('/usuario', response_class=HTMLResponse)
def get_termos(request: Request):
    return templates.TemplateResponse("arearestrita.html", {"request": request})

"""

@app.get('/usuario/alterartema', response_class=HTMLResponse)
def get_termos(request: Request):
    return templates.TemplateResponse("alterartema.html", {"request": request})

"""

@app.get('/usuario/alterartema', response_class=HTMLResponse)
def getTemas(request: Request):
    with open("temas.txt", "r", encoding="UTF-8") as arquivo:
        temas = arquivo.read().splitlines()
    return templates.TemplateResponse('alterartema.html', {'request': request, "temas": temas})

@app.post('/usuario/alterartema')
def setTemas(request: Request, tema: str = Form()):
    resposta = RedirectResponse('/usuario/alterartema', status.HTTP_302_FOUND)
    resposta.set_cookie(key="tema", value=tema.lower(), httponly=True, expires="2099-01-01T00:00:00Z")
    return resposta

@app.get('/usuario/alterarsenha', response_class=HTMLResponse)
def get_termos(request: Request):
    return templates.TemplateResponse("alterarsenha.html", {"request": request})

@app.get('/usuario/alterardados', response_class=HTMLResponse)
def get_termos(request: Request):
    return templates.TemplateResponse("alterardados.html", {"request": request})



