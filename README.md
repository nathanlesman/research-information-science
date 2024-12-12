## General information, describing your project (i.e., the abstract)
This project investigates the influence of ancient philosophical texts on shaping modern linguistic theories, with a focus on discussions from philosophers such as Plato and Aristotle. By analyzing these early works alongside contemporary linguistic frameworks, the study explores the continuity between historical and modern approaches to semantics, syntax, and pragmatics. Using texts sourced from Project Gutenberg, the research examines how exposure to ancient linguistic thought enhances comprehension of core linguistic principles in an educational context. The findings aim to highlight the enduring relevance of classical philosophy in understanding modern linguistic theories.
  
## Background information
**Plato’s Cratylus on Language Philosophy**
Plato's dialogue Cratylus delves into the nature of names and their relationship to objects, laying foundational ideas about semantics that resonate in modern linguistic debates. His exploration of whether words have a natural or conventional connection to their meanings remains influential in the study of linguistic signs.

## Research question and hypotheses 
**Research Question:**
To what extent do the linguistic structures and conceptual frameworks found in Plato's Cratylus and Aristotle's The Categories align with principles in modern linguistic theories, specifically in semantics, syntax, and pragmatics?

**Hypothesis:**
The linguistic structures and conceptual patterns in Cratylus and The Categories exhibit significant alignment with modern linguistic principles in semantics, syntax, and pragmatics.
Quantitative analysis will reveal statistically significant overlaps in lexical diversity, syntactic complexity, and semantic field distributions between ancient and modern linguistic texts.

## Method
**1. Preprocessing the Texts:**
Before analysis, the texts from ancient and modern sources need to be standardized and cleaned. Preprocessing steps include:
Tokenization: Split texts into words, sentences, or phrases for detailed analysis using bash scripts.
Stopword Removal: Remove common function words (e.g., "and," "the") that do not contribute to meaning, especially for syntactic and semantic analysis.
Stemming/Lemmatization: Normalize words to their root form (e.g., "running" → "run").
Punctuation and Number Removal: Strip out non-linguistic characters unless directly relevant to the analysis.

**2. Semantic Analysis:**
Latent Semantic Analysis (LSA):
Apply LSA to extract and compare semantic topics in the ancient texts (Cratylus, The Categories) and modern linguistic theories.
Measure cosine similarity between the semantic vectors of key topics to identify overlaps.
Word Embeddings:
Use pre-trained models like Word2Vec, GloVe, or FastText to create vector representations of words.
Compare semantic fields of terms like "naming," "categorization," and "meaning" between the ancient and modern datasets.
Calculate similarity scores between word pairs (e.g., "name" in Plato's Cratylus vs. its modern usage).

**3. Syntactic Analysis:**
**4. Pragmatic Analysis:**
**5. Topic Modeling:**
**6. Quantitative Metrics (TTR Ratio etc.):**

## References
Plato. (1892). Cratylus (B. Jowett, Trans.). Clarendon Press. (Original work published ca. 360 BCE)


Aristotle. (n.d.). The categories (E. M. Edghill, Trans.). Project Gutenberg. https://www.gutenberg.org/ebooks/2412


Secondary souces (Modern text/article/textbook):
