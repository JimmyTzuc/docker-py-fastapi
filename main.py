from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
	return {"Welcome": "Welcome to this API"}

products = []

@app.get('/products')
def get_products():
	return products
