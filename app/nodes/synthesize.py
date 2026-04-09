def generate_answer(state):
    if state.get("error"):
        return {"answer": state["error"]}

    country = state["country"]
    fields = state["fields"]
    data = state["data"]

    parts = []

    for f in fields:
        val = data.get(f)
        if val == "N/A" or val is None:
            parts.append(f"{f} is not available")
        else:
            parts.append(f"{f} is {val}")

    answer = f"For {country}, " + ", ".join(parts) + "."

    return {"answer": answer}