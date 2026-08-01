# **Fraud Detection using Neo4j and Python**

## **Project Overview**

This project demonstrates a **Fraud Detection system** on a small synthetic dataset using **Neo4j graph database** and **Python**. By modeling transactions and users as nodes and relationships, the project highlights how graph-based analytics can identify **suspicious activity and potential fraud rings**.

The project is ideal for exploring **Machine Learning, Data Science, AI, and Network Analysis concepts**, making it highly relevant for the **EMAI program**.

---

## **Key Features**

* **Graph Modeling with Neo4j**: Users and transactions represented as nodes, with relationships linking users to their transactions.
* **Fraud Metrics Analysis**: Calculate fraud ratio per user and identify high-risk accounts.
* **Network Analysis**: Centrality metrics (like betweenness) to highlight influential nodes in potential fraud networks.
* **Interactive Visualization (Matplotlib)**: Visual representation of users, transactions, and high-risk connections.
* **Synthetic Dataset Generation**: Easily reproducible dataset with multiple users, transactions, and random fraud labels.

---

## **Technologies Used**

* **Python Libraries**:

  * `py2neo` – to interact with Neo4j database
  * `networkx` – graph creation and analysis
  * `matplotlib` – network and fraud visualization
  * `pandas` – data manipulation
  * `faker` – generating synthetic user and transaction data

* **Database**: Neo4j Aura (Cloud-hosted Neo4j instance)

---

## **Installation & Setup**

1. Install Python 3.8+
2. Install required packages:

```bash
pip install py2neo pandas networkx matplotlib faker
```

3. Connect to your Neo4j Aura instance:

```python
from py2neo import Graph

graph = Graph("neo4j+s://<YOUR_URI>", auth=("neo4j", "<YOUR_PASSWORD>"))
```

---

## **How to Run**

1. Generate synthetic user-transaction dataset.
2. Push dataset to Neo4j.
3. Run **fraud analytics queries** in Neo4j to calculate fraud ratio per user.
4. Build **network graph** and visualize it using **Matplotlib**.
5. Identify **top high-risk users** using fraud ratio and network centrality.

---

## **Project Structure**

* `fraud_detection.ipynb` – main Jupyter notebook containing:

  * Synthetic data generation
  * Neo4j connection and data upload
  * Fraud analytics queries
  * Network analysis and visualization
  * Identification of high-risk users

* `README.md` – project description and instructions.

---

## **Fraud Analytics**

* **Fraud Ratio** = Number of fraudulent transactions / Total transactions per user
* **High-Risk Users** = Users with high fraud ratio and central position in the network

Example Output:

| User | Total Transactions | Fraud Transactions | Fraud Ratio |
| ---- | ------------------ | ------------------ | ----------- |
| U5   | 10                 | 3                  | 0.3         |
| U3   | 8                  | 2                  | 0.25        |

---

## **Why This Project is Relevant for EMAI**

* Demonstrates **Machine Learning & Data Science skills** through analysis of transactional data.
* Uses **Artificial Intelligence techniques** by modeling and analyzing user-transaction networks.
* Provides **hands-on experience with graph databases** (Neo4j), relevant for complex intelligent systems.
* Showcases ability to **analyze patterns, detect anomalies, and visualize results**, essential for real-world AI applications.

---

## **Next Steps / Extensions**

* Integrate a **Machine Learning model** to predict fraud probability based on graph features.
* Expand dataset to **real-world transactions** for larger scale testing.
* Include **time-series analysis** to detect suspicious trends over time.
* Develop an **interactive dashboard** for monitoring and reporting fraud in real-time.
