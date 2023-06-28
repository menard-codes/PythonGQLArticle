# Python GraphQL API with FastAPI, Strawberry, and Postgres

This project is part of the article I wrote for [ThePythonCode.com](https://thepythoncode.com).

It is a tutorial on how to build a GraphQL API in Python using FastAPI (for route handling), Strawberry (for Schema definition and everything GraphQL), and Postgres (the database).

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

6. Run the server

   ```bash
   uvicorn main:app --reload
   ```

7. Open [http://localhost:8000/graphql](http://localhost:8000/graphql) in your browser.
