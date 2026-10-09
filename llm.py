import os
from huggingface_hub import InferenceClient
MODEL = "Qwen/Qwen2.5-72B-Instruct"
def generate_response(prompt,temperature=0.2,max_tokens=500):
    hf_token = os.getenv("HF_TOKEN")
    if not hf_token:
        raise RuntimeError(
            "HF_TOKEN is not set. "
            "Add your Hugging Face API token "
            "as an environment variable."
        )
    client = InferenceClient(
        api_key=hf_token
    )
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful educational assistant. "
                    "Answer accurately and clearly for college students."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content