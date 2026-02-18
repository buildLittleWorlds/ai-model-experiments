# AI Model Experiments

A 12-session hands-on curriculum for learning how AI models work by running them, breaking them, comparing them, and reading their documentation. Every session puts a real Hugging Face model in your hands.

## What This Course Teaches

This course builds conceptual understanding of AI through direct experimentation with models from the [Hugging Face Hub](https://huggingface.co/models). Each session includes:

- **Running models in code** -- load a pipeline, feed it input, interpret the output
- **Exploring the Hub** -- browse models by task, compare download counts, find alternatives
- **Reading model cards** -- investigate training data, supported languages, known limitations, and bias disclosures
- **Swapping models** -- replace a hardcoded model ID with one you found yourself and compare results
- **Understanding failure** -- discover what makes models break and why that matters

By Session 12, students have used 15+ distinct models across text classification, summarization, generation, named entity recognition, image captioning, zero-shot classification, and question answering -- all on free Google Colab CPU.

---

## Session Notebooks

Click any badge to open the notebook directly in Google Colab.

### Foundations (Sessions 1-3)

| Session | Topic | Notebook |
|---------|-------|----------|
| 1 | From Rules to Models | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/ai-model-experiments/blob/main/session-01.ipynb) |
| 2 | Running Models with Code | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/ai-model-experiments/blob/main/session-02.ipynb) |
| 3 | Data Cleaning and Feature Engineering | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/ai-model-experiments/blob/main/session-03.ipynb) |

### Deep Understanding (Sessions 4-8)

| Session | Topic | Notebook |
|---------|-------|----------|
| 4 | How Machines Learn | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/ai-model-experiments/blob/main/session-04.ipynb) |
| 5 | Model Training and Parameters | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/ai-model-experiments/blob/main/session-05.ipynb) |
| 6 | Model Evaluation and Metrics | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/ai-model-experiments/blob/main/session-06.ipynb) |
| 7 | Overfitting and Generalization | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/ai-model-experiments/blob/main/session-07.ipynb) |
| 8 | Bias, Variance, and Uncertainty | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/ai-model-experiments/blob/main/session-08.ipynb) |

### Building (Sessions 9-10)

| Session | Topic | Notebook |
|---------|-------|----------|
| 9 | From Single Models to Systems | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/ai-model-experiments/blob/main/session-09.ipynb) |
| 10 | Prompt Logic and Human-AI Interaction | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/ai-model-experiments/blob/main/session-10.ipynb) |

### Project (Sessions 11-12)

| Session | Topic | Notebook |
|---------|-------|----------|
| 11 | Independent Project | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/ai-model-experiments/blob/main/session-11.ipynb) |
| 12 | Reflection and Level 3 Preparation | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/ai-model-experiments/blob/main/session-12.ipynb) |

---

## Recurring Notebook Features

Each notebook includes some combination of:

| Feature | What It Does |
|---------|-------------|
| **Find a Model** | Direct link to the Hugging Face Hub filtered by task -- students browse, compare, and pick a model |
| **Read the Model Card** | Guided questions about a specific model's training data, languages, and limitations |
| **Swap Slot** | A `my_model = "PASTE YOUR MODEL ID HERE"` cell where students load their own model and compare |
| **Student Input** | `student_text = "REPLACE WITH STUDENT SUGGESTION"` placeholders for live class participation |
| **Ask AI About This** | Prompts for copying code into Claude or ChatGPT to ask follow-up questions |

---

## Tools and Requirements

- **Google Colab** (free CPU tier) -- no local setup required
- **Hugging Face Transformers** (pinned to `4.47.1`)
- **Gradio** (Sessions 3, 6, 9) -- for building shareable web apps from models
- No GPU-only models -- everything runs on free Colab CPU

---

*Youth Horizons AI Researcher Program*
