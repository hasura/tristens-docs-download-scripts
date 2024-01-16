from openai import OpenAI

client = OpenAI(api_key="")

MODEL = "ft:gpt-3.5-turbo-1106:hasurahq::8XDepbEo"

assistant = client.beta.assistants.create(
    name="gpt-3.5-turbo-1106 BLOGGER",
    model=MODEL,
    tools=[],
    instructions="You are a blogger for the Hasura Blog."
)

print(assistant)
print(assistant.id)
