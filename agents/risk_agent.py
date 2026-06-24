
from llm_client import generate_response


class RiskAgent:

    def analyze(self, startup_idea):

        prompt = f"""
        You are an expert startup risk analyst.

        Analyze the startup idea:

        {startup_idea}

        Provide:

        1. Technical Risks
        2. Market Risks
        3. Financial Risks
        4. Legal Risks
        5. Operational Risks
        6. Risk Severity Assessment
        7. Mitigation Strategies

        Format professionally.
        """

        return generate_response(prompt)
