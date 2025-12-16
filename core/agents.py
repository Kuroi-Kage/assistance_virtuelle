from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

class AgentIntent:
    def __init__(self):
        self.vectorizer = TfidfTransformer()
        
    def score(self, text, memory_texts):
        """text: message utilisateur
        
        memory_texts: liste de textes depuis la memoire
        """
        # Cas mémoire vide
        if not memory_texts:
            return{
                "intent": "unknown",
                "score": 0.0,
                "reason": "memoire vide"
            }
            
        corpus = memory_texts + [text]
            
        vectors = self.vectorizer.fit_transform(corpus)
        similarities = cosine_similarity(vectors[-1], vectors[:-1])
            
        max_score = similarities.max()
            
        intent = "question" if "?" in text else "statement"
            
        return {
            "intent": intent,
            "score": float(max_score),
            "reason":"similarité sémantique TF-IDF"
         }