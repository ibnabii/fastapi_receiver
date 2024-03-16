import uvicorn


if __name__ == "__main__":
    print("Running via 'run.py'!")
    uvicorn.run(reload=True, app="src.main:app")
