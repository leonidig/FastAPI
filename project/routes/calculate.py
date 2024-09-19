from fastapi import HTTPException
import random
from .. import app


def random_message() -> str:
    messages = [
        'Wow! That was powerful!',
        'You are a real math ninja!',
        'Plus one to your math skills!',
        'Great! You are on fire!',
        'There you go, you beat the numbers again.'
    ]

    return random.choice(messages)


@app.get("/calculate/{query}")
def calculate(query: str):
    query = query.replace(" ", "")
    
    if "+" in query:
        num1, num2 = query.split("+")
        result = float(num1) + float(num2)
        
    elif "-" in query:
        num1, num2 = query.split("-")
        result = float(num1) - float(num2)

    elif "*" in query:
        num1, num2 = query.split("*")
        result = float(num1) * float(num2)

    elif ":" in query:
        num1, num2 = query.split(":")
        if num2 == "0":
            raise HTTPException(status_code=400, detail="Divide by zero? Are you serious?")
        result = float(num1) / float(num2)
    else:
        raise HTTPException(status_code=400, detail="What kind of operation is this? Try it again!")
    
    return {"result": result, "message": random_message()}
