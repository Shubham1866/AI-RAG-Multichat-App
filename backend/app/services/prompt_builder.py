def build_prompt(
    question: str,
    context_chunks: list[str],
    chat_history: list[dict]
) -> list[dict]:

    system_prompt = {
        "role": "system",
        "content": (
            "You are a helpful AI assistant. "
            "Answer strictly based on the provided context. "
            "If the answer is not in the context, say you don't know."
        )
    }

    messages = [system_prompt]

    # Add chat history
    for msg in chat_history:
        messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    # Add retrieved context
    context_text = "\n\n".join(context_chunks)
    messages.append({
        "role": "system",
        "content": f"Context:\n{context_text}"
    })

    # Add current question
    messages.append({
        "role": "user",
        "content": question
    })

    return messages