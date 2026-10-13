# Bilingual (English/Arabic) Enterprise Contract Intelligence & Compliance System

This project handles unstructured data, utilizes advanced NLP/LLMs, and implements the use of a full MLOps deployment pipeline. Below is the architecture overview: 

[insert the flowchart]

## Phase 1: Data Engineering, Cleaning, and Vectorization 

We'll be building an automated document ingestion script. The notebook '[pipeline.ipynb](pipeline.ipynb)' is a python script ready to ingest raw corporate documents. This script handles the dual-language text cleanup, embeds the text using a multilingual transformer, and indexes it into a local vector store. 

Before analyzing the text, the script cleans up spelling variations in Arabic that break standard search engines. We require the use of Regular Expressions (re) to 
1) Strip Diacritics (Tashkeel): Remove accent marks like Fatha, Damma, and Kasra. For ex, changing كِتَابٌ to كتاب
2) Standardize Alef Variants: Converts variations of Alef (أ, إ, آ) into a plain Alef (ا).

Secondly, we load LaBSE (Language-Agnostic BERT Sentence Embedding). This pre-trained AI model maps text from over 109 languages into a shared vector space. So an English sentence and its Arabic translation will yield vectors that sit very closely numerically. Lastly, we use the FAISS Vector Database. This performs an L2 distance search (Euclidean distance) which scans the database to find the vectors that are closest to the query vector.

## Phase 2: Model Tracking & Extraction Lifecycle

This is where we apply deep learning to solve a text-based business problem. The '[train_and_track.ipynb](train_and_track.ipynb)' script uses MLflow to track a sequence classification/NER task on clauses, registering parameters and performance outputs before production deployment. 

[insert model run from MLflow] 

This script is a Machine Learning experiment tracking pipeline using MLflow and Scikit-Learn. It simulates training a classification model to categorize compliance document clauses into two risk categories (0 for Low Risk, 1 for High Risk). 

## Phase 3: Production Deployment Service

We're preparing a production-ready FastAPI application wrapper providing compliance evaluations using trained pipeline components. The script '[app.ipynb](app.ipynb)' sets up a REST API using FastAPI for evaluating risk in bilingual compliance documents. 

[we show the interface and the execution]

## Phase 4: Containerized Deployment via REST API

The system is fully containerized using Docker and exposes a production-ready REST API built with FastAPI. Navigate and execute this folder '[Dockerfile](Dockerfile)'. Once the container is running safely, open your web browser and navigate to "http://localhost:8000/docs". This launches the built-in **Swagger UI** dashboard for live endpoint testing. 

[insert the UI]

Now, expand the 'Post /analyze' endpoint and click "Try it out".
Paste the following bilingual structural JSON payload into the request body :
```json
{
  "document_id": "SAAL_DOC_001",
  "text": "تم إبرام هذه الاتفاقية بين الشركة س والشريك ص لتنظيم الخدمات البنكية.",
  "language": "ar"
}
```

Click "execute" and the system successfully applies Arabic normalization rules, extracts vector features, and returns a verified server response with a '200 OK' status.
