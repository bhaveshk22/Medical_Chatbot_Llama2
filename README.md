
# Medical Chatbot Llama2

This repository contains the code for the Medical Chatbot Llama2, a sophisticated AI-powered chatbot designed to provide medical information and assistance. The project leverages advanced models and frameworks to ensure accurate and efficient performance.

## Screenshots



## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Models and Technologies](#models-and-technologies)
- [Lessons Learned](#lessons-learned)
- [License](#license)

## Features
- Utilizes the `all-MiniLM-L6-v2` model from Hugging Face for embeddings.
- Employs Pinecone Vector Database with cosine similarity for indexing and searching.
- Integrates the `llama-2-7b-chat.ggmlv3.q4_0.bin` model for chatbot responses.
- Offers an experimental option to use `PineconeHybridSearchRetriever` with dotproduct metric, available in `hybridSearch.ipynb`.
- Beautifully designed and implemented with Flask.

## Installation

### Prerequisites
- Python 3.8 or higher
- Flask
- Hugging Face Transformers
- Pinecone
- Llama 2 model files

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/bhaveshk22/Medical_Chatbot_Llama2.git
    cd medical-chatbot-llama2
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up Pinecone:
    - Create a Pinecone account and get your API key.
    - Set up your Pinecone index with cosine similarity.

4. Download the `llama-2-7b-chat.ggmlv3.q4_0.bin` model file and place it in the model directory.

## Usage

### Storing the Index
- Run the store_index.py:
    ```bash
    python store_index.py
    ```

### Running the Chatbot
1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:8080/` to interact with the chatbot.

### Using PineconeHybridSearchRetriever (Experimental)
1. Open `hybridSearch.ipynb` in your preferred Jupyter Notebook environment.
2. Follow the instructions to set up and test the `PineconeHybridSearchRetriever` with dotproduct metric.

## Models and Technologies
- **Hugging Face Embeddings Model:** `all-MiniLM-L6-v2`
  - Used for generating embeddings for text.
- **Pinecone Vector Database:**
  - Stores the embeddings and performs similarity search with cosine metric.
- **Chatbot Model:** `llama-2-7b-chat.ggmlv3.q4_0.bin`
  - Generates responses based on user input.
- **Flask:**
  - Provides a web interface for interacting with the chatbot.

## Lessons Learned
Throughout the development of the Medical Chatbot Llama2, several key lessons were learned:

1. **Model Selection:** Choosing the right model for embeddings and chatbot responses significantly impacts performance and accuracy. The `all-MiniLM-L6-v2` model from Hugging Face and the `llama-2-7b-chat.ggmlv3.q4_0.bin` model provided a good balance of speed and accuracy.

2. **Vector Database Efficiency:** Pinecone's vector database with cosine similarity proved to be efficient for storing and retrieving embeddings. Experimenting with the `PineconeHybridSearchRetriever` and different metrics like dotproduct can further optimize performance.

3. **Flask Integration:** Integrating advanced AI models with Flask for the web interface required careful consideration of API design and asynchronous processing to handle user interactions smoothly.

4. **Scalability Considerations:** As the complexity of the chatbot increases, considerations for scaling the application, such as load balancing and distributed computing, become critical to maintain performance.

5. **User Experience:** A well-designed user interface significantly enhances user interaction and satisfaction. Iterative testing and feedback helped refine the Flask-based web interface to be more intuitive and responsive.


## License
This project is licensed under the MIT License.
