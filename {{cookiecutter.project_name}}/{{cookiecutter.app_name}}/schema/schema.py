from datetime import datetime
from pydantic import BaseModel


class ExampleSchema(BaseModel):
    
    example_id : str
    content : str
    create_at : datetime