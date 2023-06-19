from . import models, database

# Will create the Table/s if they don't exist yet
models.Base.metadata.create_all(bind=database.engine)
