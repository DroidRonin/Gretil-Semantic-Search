# query/embeddings.py
import torch
from transformers import T5Tokenizer, T5EncoderModel

def load_byt5(model_name="buddhist-nlp/byt5-sanskrit", device=None):
    """loads the byt5 sanskrit model for its embeddings"""
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5EncoderModel.from_pretrained(model_name).to(device).eval()
    return tokenizer, model, device

@torch.no_grad()
def embed_query(text, tokenizer, model, device, max_length=512):
    """encoding the text into ByT5 embedding."""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=max_length).to(device)
    outputs = model(**inputs)
    vec = outputs.last_hidden_state.mean(dim=1)
    vec = torch.nn.functional.normalize(vec, p=2, dim=1)
    return vec.squeeze(0).cpu().numpy().astype("float32").reshape(1, -1)
