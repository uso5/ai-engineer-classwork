import numpy as np
from prepare_data import get_embedding


def calculate_cosine_similarity(vector_a, vector_b):

    # Compute the dot product of the two vectors
    dot_product = np.dot(vector_a, vector_b)

    # Compute the L2 norms (magnitudes) of each vector
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)

    # Compute the cosine similarity
    # Note: We add a small epsilon value to the denominator for numerical stability
    epsilon = 1e-10
    cosine_similarity = dot_product / (norm_a * norm_b + epsilon)

    return cosine_similarity


def search_text(df, search_text, n=3, pprint=True):
    embedding = get_embedding(search_text, model="text-embedding-3-small")
    df["similarities"] = df.embedding.apply(
        lambda x: calculate_cosine_similarity(x, embedding)
    )
    res = df.sort_values("similarities", ascending=False).head(n)
    return res
