# IDS 721 Miniproject 9

## Requirments
- Create a website using Streamlit
- Connect to an open source LLM (Hugging Face)
- Deploy model via Streamlit or other service (accessible via browser)

## Specification

### StreamLit
To implement the app, I used StreamLit, which is bascially using python to construct a website framework with high-efficiency. My StreamLit app is quite neat, with two pages: one page of LLM chatbot and one page of website description.

### LLM Model

I applied the text genration model from EletherAI of Hugging Face:

```
from transformers import pipeline
text_generation_pipeline = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")
```

It is actually a pretty dumb model that runs locally and only pruduce some nonsense reply. But, that's fine.

### Deployment

I push the code and enviroment to gitHub and used the StreamLit platform to deploy the app.

You can access the app through: http://152.3.65.158:8501 
