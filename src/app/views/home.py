import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get('/')
@template(template_file='index.html')
def index(user: str = 'anon'):
    return {
        'user_name': user
    }


@router.get('/about')
def about():
    return {}
