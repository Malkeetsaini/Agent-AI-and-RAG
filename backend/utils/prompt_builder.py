def build_prompt(

    memory,

    recent_messages,

    current_message
):

    return f"""
    User Memory:

    {memory}

    Recent Conversation:

    {recent_messages}

    Current Message:

    {current_message}
    """