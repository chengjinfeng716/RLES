
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


def calc_semantic_reward(queries, responses):

    score = []
    for q, r in zip(queries, responses):

        q_embeddings = model.encode(q)
        r_embedding = model.encode(r)
        sim = model.similarity(q_embeddings, r_embedding)

        score.append(sim[0][0])

    return score

