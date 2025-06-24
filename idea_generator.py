from transformers import pipeline

# Load GPT-2 model for text generation
generator = pipeline("text-generation", model="distilgpt2")

def generate_rnd_ideas(prompt, num_ideas=3):
    full_prompt = f"Suggest innovative R&D ideas for the following problem:\n{prompt}\n\nIdeas:"
    results = generator(full_prompt, max_length=150, num_return_sequences=num_ideas, do_sample=True)
    return [r['generated_text'].split("Ideas:")[-1].strip() for r in results]
