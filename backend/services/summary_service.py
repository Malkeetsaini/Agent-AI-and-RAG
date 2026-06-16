import os
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_summary(
    old_summary,
    new_messages
):

    prompt = f"""
    Existing Summary:

    {old_summary}

    New Conversation:

    {new_messages}

    Update the summary.

    Keep:
    - user preferences
    - products viewed
    - cart discussions
    - pending actions

    Return only summary.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
