from fastapi import FastAPI  # Correct

app = FastAPI()

@app.post('/blog')
def create():
    return 'creating'
