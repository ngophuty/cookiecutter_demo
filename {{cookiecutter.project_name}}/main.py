from {{cookiecutter.file_env_name}} import env


import uvicorn
from fastapi import FastAPI

app = FastAPI()

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
