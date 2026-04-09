def dynamic_prompt(input_text):
    return f"You are a smart assistant. Answer clearly: {input_text}"

def tool_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Tool error: {str(e)}"
    return wrapper

def human_in_the_loop(response):
    print("AI Response:", response)
    approval = input("Approve? (yes/no): ")
    return response if approval == "yes" else "Response rejected"