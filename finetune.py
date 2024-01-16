from openai import OpenAI

client = OpenAI(api_key="")

FILE = "miniblogrss.jsonl"

file = client.files.create(
    file=open(FILE, "rb"),
    purpose="fine-tune"
)

job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-3.5-turbo-1106"
)

print(job)
print(job.id)
