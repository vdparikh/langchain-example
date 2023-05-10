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


### Output

```
llama.cpp: loading model from ./models/ggml-model-q4_0.bin
llama.cpp: can't use mmap because tensors are not aligned; convert to new format to avoid this
llama_model_load_internal: format     = 'ggml' (old version with low tokenizer quality and no mmap support)
llama_model_load_internal: n_vocab    = 32000
llama_model_load_internal: n_ctx      = 1024
llama_model_load_internal: n_embd     = 4096
llama_model_load_internal: n_mult     = 256
llama_model_load_internal: n_head     = 32
llama_model_load_internal: n_layer    = 32
llama_model_load_internal: n_rot      = 128
llama_model_load_internal: ftype      = 2 (mostly Q4_0)
llama_model_load_internal: n_ff       = 11008
llama_model_load_internal: n_parts    = 1
llama_model_load_internal: model size = 7B
llama_model_load_internal: ggml ctx size = 4113748.20 KB
llama_model_load_internal: mem required  = 5809.33 MB (+ 2052.00 MB per state)
...................................................................................................
.
llama_init_from_file: kv self size  = 1024.00 MB
AVX = 1 | AVX2 = 1 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | FMA = 1 | NEON = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 0 | SSE3 = 1 | VSX = 0 | 
Using embedded DuckDB with persistence: data will be stored in: db_1
Security by design is a concept that emphasizes the importance of incorporating security measures into the design and development of systems, applications, and products from the very beginning of the process. It aims to integrate security as a fundamental part of the development lifecycle, rather than treating it as an afterthought or add-on.
The idea behind security by design is to minimize the risk of security vulnerabilities and threats by designing products and systems with security in mind from the start. This means considering security requirements and best practices at every stage of the design and development process, from the initial planning and architecture design to the final testing and deployment.

llama_print_timings:        load time = 432661.17 ms
llama_print_timings:      sample time =     0.00 ms /     1 runs   (    0.00 ms per run)
llama_print_timings: prompt eval time = 432660.68 ms /    68 tokens ( 6362.66 ms per token)
llama_print_timings:        eval time =     0.00 ms /     1 runs   (    0.00 ms per run)
llama_print_timings:       total time = 432666.34 ms

llama_print_timings:        load time = 432661.17 ms
llama_print_timings:      sample time =     0.00 ms /     1 runs   (    0.00 ms per run)
llama_print_timings: prompt eval time = 443816.00 ms /    66 tokens ( 6724.48 ms per token)
llama_print_timings:        eval time =     0.00 ms /     1 runs   (    0.00 ms per run)
llama_print_timings:       total time = 443833.23 ms
ingestion completed
What is security by design?
gptj_model_load: loading model from './models/ggml-gpt4all-j-v1.3-groovy.bin' - please wait ...
gptj_model_load: n_vocab = 50400
gptj_model_load: n_ctx   = 2048
gptj_model_load: n_embd  = 4096
gptj_model_load: n_head  = 16
gptj_model_load: n_layer = 28
gptj_model_load: n_rot   = 64
gptj_model_load: f16     = 2
gptj_model_load: ggml ctx size = 4505.45 MB
gptj_model_load: memory_size =   896.00 MB, n_mem = 57344
gptj_model_load: ................................... done
gptj_model_load: model size =  3609.38 MB / num tensors = 285
sending query

llama_print_timings:        load time = 432661.17 ms
llama_print_timings:      sample time =     0.00 ms /     1 runs   (    0.00 ms per run)
llama_print_timings: prompt eval time = 460945.11 ms /     7 tokens (65849.30 ms per token)
llama_print_timings:        eval time =     0.00 ms /     1 runs   (    0.00 ms per run)
llama_print_timings:       total time = 460950.06 ms
[2023-05-10 22:40:14,826] {chroma.py:128} ERROR - Chroma collection langchain contains fewer than 4 elements.
[2023-05-10 22:40:14,826] {chroma.py:128} ERROR - Chroma collection langchain contains fewer than 3 elements.
 Security by design is a concept that emphasizes the importance of incorporating security measures into the design and development of systems, applications, and products from the very beginning of the process. It aims to integrate security as a fundamental part of the development life cycle, rather than treating it as an afterthought. Security by design aims to minimize the risk of security vulnerabilities and threats by designing products and systems with security in mind from the very start of the development process. It emphasizes that the process must start with a strong commitment to security from everyone involved.

Note that in some contexts, such as information technology or other specialized domains, "design" is also known as "engineering". It refers to the entire design-related activities in those contexts. So in information technology or information system domain, security design also include other related activities like application, software design, architecture design and also product development design and life cycle.

This question could also be worded like, What is security engineering, which includes a combination of different roles that contribute to a complete development cycle in software, application or other areas that must all work in concert with the project and/or customer objectives, with security considerations woven in, all throughout?
The main principle of Security by Design is that designing for security from the outset, Security by design is a concept that emphasizes the importance of incorporating security measures into the design and development of systems, applications, and products from the very beginning of the process. It aims to integrate security as a fundamental part of the development life cycle, rather than treating it as an afterthought. Security by design aims to minimize the risk of security vulnerabilities and threats by designing products and systems with security in mind from the very start of the development process. It emphasizes that the process must start with a strong commitment to security from everyone involved.

Note that in some contexts, such as information technology or other specialized domains, "design" is also known as "engineering". It refers to the entire design-related activities in those contexts. So in information technology or information system domain, security design also include other related activities like application, software design, architecture design and also product development design and life cycle.

This question could also be worded like, What is security engineering, which includes a combination of different roles that contribute to a complete development cycle in software, application or other areas that must all work in concert with the project and/or customer objectives, with security considerations woven in, all throughout?
The main principle of Security by Design is that designing for security from the outset,
```
