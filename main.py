from fastapi import FastAPI
from graphql_server import graphql_app


app = FastAPI()
app.include_router(graphql_app, prefix='/graphql')
