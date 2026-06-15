class RankingAlgorithm:
    """
    Implements a generic item ranking algorithm using a Weighted Scoring approach.
    This class is designed to rank items based on a set of predefined weights 
    and user-specific features.
    """

    def __init__(self, weights: dict = None):
        """
        Initializes the RankingAlgorithm with optional weight configurations.

        Args:
            weights (dict, optional): A dictionary where keys are feature names 
                                      (e.g., 'popularity', 'user_affinity') and values 
                                      are their corresponding weights (float). Defaults to None.
        """
        self.weights = weights if weights is not None else {
            'popularity': 0.5,
            'user_affinity': 0.3,
            'recency': 0.2
        }

    def calculate_score(self, item: dict, user_context: dict) -> float:
        """
        Calculates a composite score for an item based on its features and the user context.

        Args:
            item (dict): A dictionary representing the item to be scored. 
                         Expected keys might include 'id', 'name', 'price', etc.
            user_context (dict): A dictionary containing relevant user data, 
                                 e.g., {'preferences': {...}, 'history': [...]}

        Returns:
            float: The calculated composite score for the item.
        """
        score = 0.0

        # 1. Popularity Score (Example feature)
        popularity_factor = self.weights.get('popularity', 0.5)
        # Assuming 'item' has a 'popularity_score' key or similar metric
        item_popularity = item.get('popularity_score', 1.0) 
        score += popularity_factor * item_popularity

        # 2. User Affinity Score (Example feature)
        affinity_factor = self.weights.get('user_affinity', 0.3)
        # Assuming 'item' has a 'user_affinity_match' key or similar metric
        item_affinity = item.get('user_affinity_match', 1.0)
        score += affinity_factor * item_affinity

        # 3. Recency Score (Example feature)
        recency_factor = self.weights.get('recency', 0.2)
        # Assuming 'item' has a 'last_updated' key or similar metric
        item_recency = item.get('recency_score', 1.0)
        score += recency_factor * item_recency

        return score

    def rank_items(self, items: list[dict], user_context: dict, top_n: int = 10) -> list[tuple[dict, float]]:
        """
        Ranks a list of items based on the calculated composite score.

        Args:
            items (list[dict]): A list of item dictionaries to rank.
            user_context (dict): The context data for the user.
            top_n (int): The number of top-ranked items to return.

        Returns:
            list[tuple[dict, float]]: A list of tuples, where each tuple contains 
                                      the item dictionary and its calculated score, sorted descending by score.
        """
        scored_items = []
        for item in items:
            score = self.calculate_score(item, user_context)
            scored_items.append((item, score))

        # Sort items by score in descending order
        scored_items.sort(key=lambda x: x[1], reverse=True)

        return scored_items[:top_n]

# --- Complexity Constraints ---
"""
Complexity Analysis:
- calculate_score: O(k), where k is the number of features used in the scoring formula (constant time relative to input size).
- rank_items: O(N log N) due to the sorting step, where N is the number of items provided. 
             If a more efficient selection method were required for very large N, 
             a selection algorithm like Quickselect could achieve O(N) average time complexity.
"""