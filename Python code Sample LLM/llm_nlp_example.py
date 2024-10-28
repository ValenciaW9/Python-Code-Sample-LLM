import openai

# Set up OpenAI API key (you would use your actual API key here)
openai.api_key = 'your-openai-api-key'

def summarize_text(text):
    """
    Function to summarize the given text using an LLM model.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following text:\n\n{text}",
        max_tokens=150,
        temperature=0.5
    )
    summary = response.choices[0].text.strip()
    return summary


def classify_text(text):
    """
    Function to classify the topic of the input text using LLM.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Classify the following text into one of the categories: 'Technology', 'Health', 'Education', 'Finance', 'Entertainment'.\n\nText: {text}\nCategory:",
        max_tokens=10,
        temperature=0.5
    )
    classification = response.choices[0].text.strip()
    return classification


def generate_response(prompt):
    """
    Function to generate a conversational response using an LLM.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7
    )
    reply = response.choices[0].text.strip()
    return reply


if __name__ == "__main__":
    # Example text to summarize and classify
    sample_text = """
    Artificial intelligence is transforming the world in many fields such as healthcare, finance, and education. 
    AI is used to predict diseases, automate trading, and provide personalized learning experiences.
    """
    
    # Summarize the text
    summary = summarize_text(sample_text)
    print(f"Summary:\n{summary}\n")
    
    # Classify the text
    category = classify_text(sample_text)
    print(f"Classified Category: {category}\n")
    
    # Generate a conversational response
    user_input = "What are the latest advancements in AI?"
    ai_response = generate_response(user_input)
    print(f"AI Response:\n{ai_response}\n")
