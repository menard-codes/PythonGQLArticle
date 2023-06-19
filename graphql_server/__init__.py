import strawberry
from strawberry.fastapi import GraphQLRouter

from .schemas import Task
from .resolvers import QueryResolver, MutationResolver

from typing import List


@strawberry.type
class Query:
    tasks: List[Task] = strawberry.field(resolver=QueryResolver.get_tasks)
    task: (Task | None) = strawberry.field(resolver=QueryResolver.get_task)


@strawberry.type
class Mutation:
    add_task: Task = strawberry.field(resolver=MutationResolver.add_task)
    update_task: (Task | None) = strawberry.field(
        resolver=MutationResolver.update_task)
    delete_task = strawberry.field(resolver=MutationResolver.delete_task)


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
