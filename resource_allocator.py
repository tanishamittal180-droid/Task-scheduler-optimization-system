class ResourceAllocator:
    
    def assign_resource(
        self,
        task,
        resources
    ):

        skill_needed = task.get(
            "skill_required",
            "general"
        )

        for resource in resources:

            if resource.get(
                "skill",
                ""
            ).lower() == skill_needed.lower():

                return resource

        return resources[0]