import json
import faiss

def load_metadata(jsonl_path):
    """Load metadata JSONL file as list of dicts."""
    meta = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            meta.append(json.loads(line))
    return meta

def load_index(index_path):
    """to read the FAISS index from the disk: """
    return faiss.read_index(index_path)

def search_index(index, query_vec, metadata, k=5):
    """searching the index within faiss and returning top k results"""
    scores, ids = index.search(query_vec, k)
    results = []
    for rank, (idx, score) in enumerate(zip(ids[0], scores[0]), 1):
        if idx < 0:
            continue
        results.append({
            "rank": rank,
            "score": float(score),
            "source_file": metadata[idx]["source_file"],
            "chunk_id": metadata[idx]["chunk_id"],
            "text": metadata[idx]["text"]
        })
    return results
