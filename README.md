# Python GraphQL API with FastAPI, Strawberry, and Postgres

This project is part of the article I wrote for [ThePythonCode.com](https://thepythoncode.com).

You can check out the article using this link:

[https://www.thepythoncode.com/article/build-a-graphql-api-with-fastapi-strawberry-and-postgres-python](
https://www.thepythoncode.com/article/build-a-graphql-api-with-fastapi-strawberry-and-postgres-python)

It is a tutorial on how to build a GraphQL API in Python using FastAPI (for route handling), Strawberry (for Schema definition and everything GraphQL), and Postgres (the database).

## Prerequisites

If you decided to follow along the tutorial (or just to run this project), first, make sure you have:

1. [ElephantSQL Account (optional)](https://www.elephantsql.com/) - If you decided to use Postgres (like in the tutorial) and decided to go for the managed Postgres DB option
2. Python3: ^3.11.0

## Getting Starteted

1. Fork this repo.
2. Clone it in your local device.

   ```bash
   git clone git@github.com:<user>/PythonGQLArticle.git
   cd PythonGQLArticle
   ```

3. Create a virtual environment

   ```bash
   python3 -m venv pygql
   ```

4. Activate the virtual environment

   ```bash
   # MacOS/Linux
   source pygql/bin/activate

   # Windows
   pygql\Scripts\activate
   ```

5. Install the dependencies

   ```bash
   pip3 install -r requirements.txt
   ```

6. Add your Database URL - Create a `.env` file, add your DATABASE URL, and access it in the `database.py` file:

   ```bash
   # .env file
   DB_URL='<YOUR DATABASE URL HERE>'
   ```

   ```python
   # models/database.py
   ...
   SQLALCHEMY_DATABASE_URL = config("DB_URL")
   ```

7. Run the server

   ```bash
   uvicorn main:app --reload
   ```

8. Open [http://localhost:8000/graphql](http://localhost:8000/graphql) in your browser.
