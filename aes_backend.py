import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class AESBackend:
    def __init__(self):
        # Load spaCy English model
        self.nlp = spacy.load("en_core_web_sm")

    # -----------------------------------------------------
    # CONTENT SIMILARITY (TF-IDF Cosine)
    # -----------------------------------------------------
    def evaluate_content(self, reference, essay):
        if not reference.strip() or not essay.strip():
            return 0

        vectorizer = TfidfVectorizer(stop_words='english')
        vectors = vectorizer.fit_transform([reference, essay])
        similarity = cosine_similarity(vectors)[0, 1]

        return min(similarity * 30, 25)
    

    # -----------------------------------------------------
    # ORGANIZATION SCORE (Structure similarity)
    # Uses paragraph-level comparison
    # -----------------------------------------------------
    def evaluate_organization(self, reference, essay):
        ref_paragraphs = [p.strip() for p in reference.split("\n") if p.strip()]
        essay_paragraphs = [p.strip() for p in essay.split("\n") if p.strip()]

        if not ref_paragraphs or not essay_paragraphs:
            return 0

        vectorizer = TfidfVectorizer(stop_words='english')

        try:
            vectors = vectorizer.fit_transform([
                " ".join(ref_paragraphs),
                " ".join(essay_paragraphs)
            ])
            similarity = cosine_similarity(vectors)[0, 1]
        except ValueError:
            similarity = 0

        return similarity * 10  # Scale to 10 marks

    # -----------------------------------------------------
    # GRAMMAR / MECHANICS (Lightweight Offline Logic)
    # -----------------------------------------------------
    def evaluate_grammar_mechanics(self, essay):
        doc = self.nlp(essay)
        total_tokens = len(doc)

        if total_tokens == 0:
            return 0

        # Simple structural checks
        double_spaces = essay.count("  ")
        repeated_punct = essay.count("..")
        no_capital_start = sum(
            1 for sent in doc.sents if sent.text and not sent.text.strip()[0].isupper()
        )
        very_short_sentences = sum(
            1 for sent in doc.sents if len(sent.text.split()) < 3
        )

        penalty = double_spaces + repeated_punct + no_capital_start + very_short_sentences

        score = max(total_tokens - penalty, 0) / total_tokens
        return score * 10  # Scale to 10 marks

    # -----------------------------------------------------
    # WORD CHOICE (Lexical Diversity using Lemmas)
    # -----------------------------------------------------
    def evaluate_word_choice(self, essay):
        doc = self.nlp(essay)

        tokens = [token.lemma_.lower() for token in doc if token.is_alpha]
        total_tokens = len(tokens)

        if total_tokens == 0:
            return 0

        unique_tokens = len(set(tokens))

        diversity_ratio = unique_tokens / total_tokens

        return diversity_ratio * 5  # Scale to 5 marks

    # -----------------------------------------------------
    # FINAL GRADING
    # -----------------------------------------------------
    def grade_essay(self, reference, essay):
        content_score = round(self.evaluate_content(reference, essay))
        organization_score = round(self.evaluate_organization(reference, essay))
        grammar_mechanics_score = round(self.evaluate_grammar_mechanics(essay))
        word_choice_score = round(self.evaluate_word_choice(essay))

        print(f"Content Score: {content_score} / 25")
        print(f"Organization Score: {organization_score} / 10")
        print(f"Grammar/Mechanics Score: {grammar_mechanics_score} / 10")
        print(f"Word Choice Score: {word_choice_score} / 5")

        total_score = (
            content_score
            + organization_score
            + grammar_mechanics_score
            + word_choice_score
        )

        print(f"Total Score: {total_score} / 50")
        return total_score
