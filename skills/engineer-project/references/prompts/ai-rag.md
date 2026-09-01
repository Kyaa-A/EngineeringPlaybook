# AI and RAG Prompts

## Choose deterministic, AI, or agentic

```text
Evaluate deterministic software, a narrow LLM step, RAG, and an agentic workflow for {{problem}} under {{constraints}}. Compare correctness, latency, cost, observability, security, maintenance, and failure behavior. Recommend the simplest sufficient option and identify every decision that must remain deterministic.
```

## RAG design

```text
Design a measurable RAG pipeline for {{documents}}, {{queries}}, {{access_model}}, and {{scale}}. Cover parsing, semantic chunking, metadata, embeddings, pgvector with HNSW, authorization-aware retrieval, hybrid search, reranking, citation-grounded generation, unanswerable behavior, deletion and re-indexing, recall at K, groundedness, citation correctness, latency, and cost.
```

## Structured prompt

```text
Create a versioned production prompt for {{task}} with input contract {{input_schema}} and output contract {{output_schema}}. Include system and user templates, representative and adversarial examples, insufficient-data behavior, one bounded repair policy, and verification cases. Do not let the model decide authorization or destructive actions.
```
