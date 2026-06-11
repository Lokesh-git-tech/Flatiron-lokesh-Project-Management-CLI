import ollama


class AIClient:

    def __init__(self, model_name="llama3.2"):
        self.model_name = model_name

    def summarize_project(self, project):

        prompt = f"""
        Project Title: {project.title}

        Description:
        {project.description}

        Due Date:
        {project.due_date}

        Tasks:
        """

        for task in project.tasks:
            prompt += (
                f"\n- {task.title}"
                f" ({task.status})"
                f" Assigned To: {task.assigned_to}"
            )

        prompt += """

Give:
1. Short Project Summary
2. Risks
3. Suggested Next Steps
"""

        try:

            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response["message"]["content"]

        except Exception:
            return "Could not generate AI summary at this time."