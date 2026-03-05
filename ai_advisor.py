from config import model

def get_financial_advice(income, expenses, savings, debt, goal):

    prompt = f"""
    A user has the following financial details:

    Monthly Income: {income}
    Monthly Expenses: {expenses}
    Current Savings: {savings}
    Current Debt: {debt}
    Financial Goal: {goal}

    Provide simple financial advice including:
    - Budgeting tips
    - Savings improvement
    - Debt management
    - Investment suggestions

    Keep the response short and clear.
    """

    response = model.generate_content(prompt)

    return response.text


def chatbot_response(question):

    prompt = f"""
    You are a financial advisor.

    Answer the user's question simply.

    Question: {question}
    """

    response = model.generate_content(prompt)

    return response.text