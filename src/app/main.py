import os
import fastapi
import uvicorn
import fastapi_chameleon
from fastapi_chameleon import template

from views import home
from views import account
from views import packages

app = fastapi.FastAPI()

dev_mode = True

folder = os.path.dirname(__file__)
template_folder = os.path.join(folder, 'templates')
template_folder = os.path.abspath(template_folder)

fastapi_chameleon.global_init(template_folder, auto_reload=dev_mode)

app.include_router(home.router)
app.include_router(account.router)
app.include_router(packages.router)


if __name__ == '__main__':
    uvicorn.run(app)
