from config import model


def chatbot_response(question):

    try:
        response = model.generate_content(question)
        return response.text

    except Exception as e:
        return f"AI chatbot error: {str(e)}"


def get_financial_advice(income, expenses, savings, debt, goal):

    prompt = f"""
    A user has the following financial details:

    Monthly Income: {income}
    Monthly Expenses: {expenses}
    Current Savings: {savings}
    Current Debt: {debt}
    Financial Goal: {goal}

    Provide short financial advice including:
    - Budgeting
    - Saving tips
    - Debt management
    - Investment suggestions
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"AI advice error: {str(e)}"
