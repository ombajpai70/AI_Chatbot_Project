from config import SIMILARITY_THRESHOLD


def filter_results(chunks, indices, scores,target_documents=None):

    context = ""
    matched_chunks = []
    seen_chunks = set()

    for idx, score in zip(indices[0], scores[0]):

        if score < SIMILARITY_THRESHOLD:
            continue
       
        if target_documents:
          if chunks[idx]["document"] not in target_documents:
              continue
        
        chunk_text = chunks[idx]["text"].strip()
        if chunk_text in seen_chunks:
          continue
        seen_chunks.add(chunk_text)
       
        matched_chunks.append(
            {   "document": chunks[idx]["document"],
                "score": float(score),
                "page": chunks[idx]["page"],
                "text": chunks[idx]["text"]
            }
        )

        context += chunks[idx]["text"]
        context += "\n\n"

        matched_chunks.sort(
        key=lambda x: x["score"],
        reverse=True
        )

    return context, matched_chunks