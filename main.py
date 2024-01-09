import uvicorn

from FastApiApp import FastApiApp


if __name__ == "__main__":
    fast_api_app = FastApiApp()
    uvicorn.run(fast_api_app.app, host="127.0.0.1", port=8000)
