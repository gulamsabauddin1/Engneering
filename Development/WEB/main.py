from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to your backend engine, Gulam! 😄"}

@app.get("/items")
def get_items():
    return ["Item A", "Item B", "Item C"]

@app.get("/username")
def calculate():
    print("Calculating username...")
    return("A=10, B=20 ",10+20)
    

   
    