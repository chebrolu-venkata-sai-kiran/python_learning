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
