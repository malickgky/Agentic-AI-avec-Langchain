from agent import create_agent

if __name__ == "__main__":
    agent = create_agent()

    while True:
        query = input("You: ")
        response = agent.run(query)
        print("AI:", response)