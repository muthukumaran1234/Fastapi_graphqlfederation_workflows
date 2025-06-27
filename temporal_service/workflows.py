from temporalio import workflow
from activities import create_user, assign_role


@workflow.defn
class CreateUserWithRoleWorkflow:
    @workflow.run
    async def run(self, user_data: dict, role_id: int) -> str:
        user_id = await workflow.execute_activity(
            create_user,
            user_data,
            schedule_to_close_timeout=10,
        )
        success = await workflow.execute_activity(
            assign_role,
            user_id,
            role_id,
            schedule_to_close_timeout=10,
        )
        return f"User created with ID {user_id} and role assignment {'succeeded' if success else 'failed'}."
