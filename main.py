"""
Using a language of your choice, write a simple HTTP endpoint to listen on http://127.0.0.1:8013/colors
This endpoint should accept an HTTP/POST where the body is a single plain text “text” object of up to 100 characters.

For every “text” received return http/200 OK if the word has been seen before. Return http/201 CREATED if the word has 
not been seen before and will be added to storage

http://127.0.0.1:8013/colors body = “red green blue YELLOW CyAn”
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI


class Textin(BaseModel):
    text: str


texts = {
}

@app.post('colors')
def check_colors(text_in: Textin):
    text = text_in.text

    if len(text) > 100:
        return HTTPException(status_code=400)
    
    text = text.upper()
    text_sliced = text.split(' ')
    

    for text in text_sliced:
        if text not in texts:
            texts[text] = True
            return {'status_code': 201, 'message': 'Color created'}
        else:
            return {'status_code': 200, 'message': 'Success'}