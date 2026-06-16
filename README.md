# AI Shopping Agent

An AI-powered e-commerce platform built with FastAPI, ReactJS, MySQL, ChromaDB, and Google Gemini.

The application supports:

* Product Catalog
* Semantic Search
* AI Shopping Agent
* Image Search
* Cart Management
* Order Management
* JWT Authentication
* Summary-Based Memory
* Tool Calling Agent

---

# Features

## Authentication

* User Registration
* User Login
* JWT Authentication
* Protected APIs

## Product Management

* Import Products from CSV
* Fashion Products
* Jewelry Products
* Bicycle Products

## Semantic Search

* ChromaDB Vector Database
* Gemini Embeddings
* Natural Language Product Search

Example:

```
Show me red bicycles
```

```
Find silver jewelry under 1000
```

## AI Shopping Agent

Supports:

* Product Search
* Add To Cart
* View Cart
* Place Order
* General Conversation

Example:

```
Show me black shoes
```

```
Add first product to cart
```

```
Place my order
```

## Image Search

Upload an image and find visually similar products.

## Summary Memory

Stores:

* Recent Messages
* Conversation Summary

Allows:

* Long-Term Context
* Reduced Token Usage
* Better Agent Responses

---

# Tech Stack

## Backend

* FastAPI
* SQLAlchemy
* MySQL
* ChromaDB
* Google Gemini
* Sentence Transformers

## Frontend

* ReactJS
* Vite
* React Router
* Axios

## AI

* Gemini 2.5 Flash
* Gemini Embedding 001
* Tool Calling Agent

---

# Project Structure

```
app/

├── backend/
│
├── frontend/
│
├── chroma_db/
│
├── csv/
│
└── uploads/
```

---

# Backend Structure

```
backend/

├── database/
├── models/
├── schemas/
├── routers/
├── services/
├── middleware/
├── embeddings/
├── memory/
├── utils/
├── uploads/
└── main.py
```

---

# Database Tables

## users

```
id
name
email
password
created_at
```

## products

```
id
title
description
price
category
image_url
vendor
```

## product_variants

```
id
product_id
sku
option_name
option_value
price
```

## product_images

```
id
product_id
image_url
```

## carts

```
id
user_id
```

## cart_items

```
id
cart_id
product_id
quantity
```

## orders

```
id
user_id
total_amount
status
```

## order_items

```
id
order_id
product_id
quantity
price
```

## chat_history

```
id
user_id
role
message
created_at
```

## memory_summary

```
id
user_id
summary
updated_at
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/ai-shopping-agent.git

cd ai-shopping-agent
```

---

# Backend Setup

Create virtual environment

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run backend

```bash
uvicorn backend.main:app --reload
```

Backend URL

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

---

# Frontend Setup

Install dependencies

```bash
npm install
```

Run frontend

```bash
npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# Import CSV Data

Place files:

```
fashion.csv
jewelry.csv
bicycle.csv
```

Run:

```bash
python -m backend.utils.csv_loader
```

Products will be imported into MySQL.

---

# Generate Embeddings

Configure:

```
GOOGLE_API_KEY
```

Run:

```bash
python -m backend.embeddings.generate_embeddings
```

Embeddings will be stored in ChromaDB.

---

# API Endpoints

## Authentication

### Register

```
POST /auth/register
```

### Login

```
POST /auth/login
```

---

## Products

### Get Products

```
GET /products
```

### Product Details

```
GET /products/{id}
```

---

## Cart

### Add To Cart

```
POST /cart/add
```

### View Cart

```
GET /cart
```

### Remove Item

```
DELETE /cart/remove/{id}
```

---

## Orders

### Place Order

```
POST /orders
```

### View Orders

```
GET /orders
```

---

## Search

### Semantic Search

```
POST /search
```

Request:

```json
{
  "query": "red bicycle"
}
```

---

## Image Search

### Upload Image

```
POST /image-search
```

---

## Chatbot

### Chat With Agent

```
POST /chat
```

Request:

```json
{
  "message": "show me red bicycles"
}
```

Response:

```json
{
  "type": "search_products",
  "answer": "...",
  "tool_result": {}
}
```

---

# Future Improvements

* Multi Vendor Marketplace
* Recommendation Engine
* Wishlist
* Payment Gateway
* Voice Agent
* RAG Product Knowledge Base
* Multi-Agent Workflow
* Admin Dashboard
* Analytics Dashboard

---

# Author

Malkeet Singh

AI Engineer | FastAPI | ReactJS | GenAI | Computer Vision
