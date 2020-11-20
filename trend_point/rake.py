from collections import Counter

from nlp_rake import Rake


def most_common_words(articles, n_themes=5, n_keywords=10, max_words_to_rake=1):
    rake = Rake(max_words=max_words_to_rake)
    keywords_frequencies = Counter()
    for article in articles:
        rake_keywords = rake.apply(article)
        for rk in rake_keywords[:n_keywords]:
            keywords_frequencies[rk[0]] += 1
    return keywords_frequencies.most_common(n_themes)

