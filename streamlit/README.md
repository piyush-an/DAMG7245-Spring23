
## Streamlit

### What is Streamlit ?
> Streamlit is an open-source app framework for Machine Learning and Data Science teams to create beautiful web apps in minutes.

### Prerequisite
* IDE
* Python 3.x

---

### Tutorial

Step 01: Create a python virtual environment and activate
```bash
python -m venv venv_streamlit
.\venv_streamlit\Scripts\activate
```

Step 02: Install python Packages
```bash
pip install streamlit
```
Step 03: Develop a python script - main.py

In this guide, you're going to use Streamlit's core features to create an interactive app; exploring a public Uber dataset for pickups and drop-offs in New York City. When you're finished, you'll know how to fetch and cache data, draw charts, plot information on a map, and use interactive widgets, like a slider, to filter results.

https://docs.streamlit.io/library/get-started/create-an-app

Step 04: Run Streamlit app
```bash
streamlit run main.py
```

Step 05: Export python dependency
```bash
pip freeze > requirements.txt
```

Step 06: Commit your code to github

**Never commit your virtual environment**. <br> 
Generate `requirements.txt` file using `pip freeze > requirements.txt` and install on the target machine by `pip install -r requirements.txt`.

Step 07: Deploy on Streamlit Cloud

https://streamlit.io/cloud