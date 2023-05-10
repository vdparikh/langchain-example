# langchain-example
This example demonstrates how to ingest custom text and query it for questions. It uses local LLM and does not need OpenAI or HuggingFace API.

### Download the models
Download below 2 files and place them in `models` directory
- Download LLM ggml-gpt4all-j-v1.3-groovy.bin
https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin
- Download Embedding model ggml-model-q4_0.bin
https://huggingface.co/Pi3141/alpaca-native-7B-ggml/resolve/397e872bf4c83f4c642317a5bf65ce84a105786e/ggml-model-q4_0.bin


### Running the Sample

```
python3 main.py
```

This will first ingest the text and persists in vector db and then executes a query to get the answer
