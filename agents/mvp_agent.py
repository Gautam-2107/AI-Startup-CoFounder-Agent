
from llm_client import generate_response


class MVPAgent:

    def analyze(self, startup_idea):

        prompt = f"""
        You are an expert startup product manager.

        Analyze the startup idea:

        {startup_idea}

        Create:

        1. MVP Goal
        2. Core Features
        3. User Flow
        4. Technology Stack Suggestions
        5. Development Roadmap
        6. Launch Plan
        7. Success Metrics

        Format professionally.
        """

        return generate_response(prompt)
