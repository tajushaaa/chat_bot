import openai

openai.api_key = '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'

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Write me an essay about AI"}])
print(completion.choices[0].message.content)
