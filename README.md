# Drug Desing Chat Bot with Llama 2 and LangChain

## Steps to Run
### 1. Create an Env.
```bash
conda create -n agi python=3.9 -y
```
```bash
conda activate agi
```
### 2. Install Libraries
```bash
pip install -r requirements.txt
```

### 3. NoteBook
All the libraries was updated to the last version to 03/2024

#### Download this model from the hugging face web
```ini
llama-2-7b-chat.ggmlv3.q4_0.bin
```
#### Create a ```.env``` file in the root directory and add your pinecone credentials
```bash
PINECONE_API_KEY = "bd8cfcb4-cbf6-4217-975f-b3c44e079668"
PIPECONDE_API_ENV = 'gcp-starter'
TOKENIZERS_PARALLELISM = False
```
Now...


