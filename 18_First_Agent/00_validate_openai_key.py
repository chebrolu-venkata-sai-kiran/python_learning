from openai import OpenAI

client = OpenAI(api_key="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")

try:
    response = client.responses.create(
        model="gpt-4",
        input="Say hello in one sentence."
    )

    print("Response:")
    print(response.output_text)

except Exception as e:
    print("Error occurred:")
    print(e)
