from transformers import pipeline

# Load smaller model for faster, reliable generation
generator = pipeline("text-generation", model="distilgpt2")

def generate_rnd_ideas(prompt, num_ideas=5):
    full_prompt = f"List {num_ideas} distinct, innovative research and development ideas related to:\n{prompt}\n\n1."
    
    results = generator(
        full_prompt,
        max_length=80,
        num_return_sequences=num_ideas,
        do_sample=True,
        temperature=0.9,
        top_p=0.9,
        repetition_penalty=1.2,
        pad_token_id=50256  # required for GPT-2 models
    )
    
    ideas = []
    for res in results:
        text = res['generated_text']
        # Remove the prompt part from the generated text
        idea_text = text.split(full_prompt)[-1].strip()
        ideas.append(idea_text)
    return ideas
