from config import model


def get_financial_advice(income, expenses, savings, debt, goal):

    try:

        prompt = f"""
        A user has the following financial details:

        Monthly Income: {income}
        Monthly Expenses: {expenses}
        Current Savings: {savings}
        Current Debt: {debt}
        Financial Goal: {goal}

        Provide short financial advice including:
        - Budgeting tips
        - Savings improvement
        - Debt management
        - Investment suggestions
        """

        response = model.generate_content(prompt)

        return response.text

    except Exception:

        return "AI service temporarily unavailable. Please try again."


def chatbot_response(question):

    try:

        prompt = f"""
        You are a helpful financial advisor.

        Answer the user's financial question clearly.

        Question: {question}
        """

        response = model.generate_content(prompt)

        return response.text

    except Exception:

        return "AI chatbot temporarily unavailable."
