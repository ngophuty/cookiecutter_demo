from {{cookiecutter.file_env_name}} import env
from fastapi.middleware.wsgi import CORSMiddleware
from {{cookiecutter.project_name}}.core.middleware.middleware import add_process_time_header

import uvicorn
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    add_process_time_header)



@app.get('/',tags=['Hello'])
async def hello_world():
    return {'message':'hello world!'}




if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host= env.HOST,
        port= env.PORT,
        reload= True
    )
