import asyncio
from temporalio.client import Client
from temporalio.worker import Worker

from workflows import CreateUserWithRoleWorkflow
import activities


async def main():
    client = await Client.connect("temporal:7233")  # This matches your docker-compose Temporal service name

    worker = Worker(
        client,
        task_queue="user-role-task-queue",
        workflows=[CreateUserWithRoleWorkflow],
        activities=[activities.create_user, activities.assign_role],
    )

    print("Starting Temporal Worker...")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
