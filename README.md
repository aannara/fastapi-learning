# Introduction to FastAPI

[![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://aannara.github.io/fastapi-learning)

### We are going to focus on understanding how to use FastAPI.

### I will cover the basics of FastAPI to creating your own projects using FastAPI.

### The course instructor will be **Aadithya Varma**.

<hr />

## ✨ Pre-requisites ✨

- Basic understanding of web servers and HTTP status codes
- Dedicated to spending time to learn Python during the live course
- Basic googling skills or using ChatGPT to get answers
- Must have installed Python in your system
- Basics of git if you want to clone this repo to follow the course in your local environment

<hr />

## ✨ What to expect from the course ✨

- Understand how to use FastAPI
- Learn the different use cases to use FastAPI
- See a completed project using FastAPI

<hr />

## ✨ Get started ✨

### Running the course contents on your local environment

1. Make sure you have Python installed. Follow the guide in the official Python documentation on how to do it for different operating systems: [Windows](https://docs.python.org/3/using/windows.html#installation-steps), [Mac](https://docs.python.org/3/using/mac.html#getting-and-installing-macpython), or [Unix](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) systems.
2. Make sure you have [Git](https://git-scm.com/downloads) installed. Clone this repository: `git clone https://github.com/aannara/fastapi-learning.git`
3. Change directory to the new one: `cd fastapi-learning`
4. Recommended creating a virtual environment to install the dependencies: `python -m venv .venv`
5. Activate virtual environment: On Windows `.venv\Scripts\activate` and on Linux `source .venv/bin/activate`
6. Install all the dependencies in the virtual environment: `pip install -r requirements.txt`
7. Run Jupyter Lab: `jupyter lab`

<img src="./static/jupyter-lab.gif" width="700">

<hr />

<h1 align="center"> Hello, I'm Aadithya Varma 👋</h1>

<pre>
💻 Working as a software engineer at Intel
🎓 Masters in Software Engineering and another Masters in Artificial Intelligence and Machine Learning
🛠️ Worked on backend application development, DevOps, SCM tools and BigData analysis
🌟 Loves to build clean, efficient and scalable systems
😃 Outside of work, I spend my time playing games, watching anime and TV shows
</pre>

<hr />

<h2 align="left">Tools I use</h2>
<p align="left">
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original-wordmark.svg" alt="Python" width="40" height="40"/>
<a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bash/bash-original.svg" alt="Bash" width="40" height="40"/> </a>
<a href="https://www.vim.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vim/vim-original.svg" alt="vim" width="40" height="40"/> </a>
<a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="Git" width="40" height="40"/> </a>
<a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/cncf/landscape/master/hosted_logos/docker-member.svg" alt="Docker" width="40" height="40"/> </a>
<a href="https://docs.sylabs.io/guides/latest/user-guide/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/sylabs/singularity/b8491424ee2d4c907c4b0817ef2eda4f95c90548/docs/logos/singularity_v3.svg" alt="Singularity" width="40" height="40"/> </a>
<a href="https://hadoop.apache.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/apache_hadoop/apache_hadoop-ar21.svg" alt="Hadoop" width="40" height="40"/> </a>
<a href="https://spark.apache.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/apache_spark/apache_spark-ar21.svg" alt="Apache Spark" width="40" height="40"/> </a>
<a href="https://kafka.apache.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/apachekafka/apachekafka-original.svg" alt="Apache Kafka" width="40" height="40"/> </a>
<a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a>
</p>
<p align="left">
<a href="https://prometheus.io/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/prometheus/prometheus-original-wordmark.svg" alt="prometheus" width="40" height="40"/> </a>
<a href="https://www.mongodb.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" alt="mongodb" width="40" height="40"/> </a>
<a href="https://redis.io/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/redis/redis-original-wordmark.svg" alt="redis" width="40" height="40"/> </a>
<a href="https://www.elastic.co/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/cncf/landscape/master/hosted_logos/elastic-member.svg" alt="elastic" width="40" height="40"/> </a>
<a href="https://www.perforce.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/perforce/perforce-ar21.svg" alt="perforce" width="40" height="40"/> </a>
<a href="https://grafana.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/grafana/grafana-original-wordmark.svg" alt="grafana" width="40" height="40"/> </a>
<a href="https://streamlit.io/" target="_blank" rel="noreferrer"> <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.svg" alt="streamlit" width="40" height="40"/> </a>
<a href="https://superset.apache.org/" target="_blank" rel="noreferrer"> <img src="https://www.apache.org/logos/res/superset/superset-2.png" alt="superset" width="40" height="40"/> </a>
<a href="https://cloud.google.com/looker" target="_blank" rel="noreferrer"> <img src="https://images.ctfassets.net/qeopvtiy4eew/5d7ZhffO1g9JpFKSXT06kB/629978a1f48ed4bd953d13401d13182a/looker-logo_200x200_square.svg" alt="looker" width="40" height="40"/> </a>
<a href="https://www.metabase.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/metabase/metabase-icon.svg" alt="metabase" width="40" height="40"/> </a>
</p>
<p align="left">
<a href="https://plotly.com/graphing-libraries/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/plot_ly/plot_ly-official.svg" alt="plotly" width="40" height="40"/> </a>
<a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a>
<a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/fastapi/fastapi-original.svg" alt="FastAPI" width="40" height="40"/> </a>
<a href="https://www.jenkins.io" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/jenkins/jenkins-icon.svg" alt="jenkins" width="40" height="40"/> </a>
<a href="https://www.ansible.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/ansible/ansible-original-wordmark.svg" alt="ansible" width="40" height="40"/> </a>
<a href="https://aws.amazon.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" height="40"/> </a>
<a href="https://github.com/features/actions" target="_blank" rel="noreferrer"> <img src="https://github.githubassets.com/images/modules/site/features/actions-icon-actions.svg" alt="GitHub Actions" width="40" height="40"/> </a>
<a href="https://docs.pytest.org/en/latest/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pytest/pytest-original-wordmark.svg" alt="pytest" width="40" height="40"/> </a>
<a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original-wordmark.svg" alt="pandas" width="40" height="40"/> </a>
<a href="https://www.tensorflow.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/tensorflow/tensorflow-original.svg" alt="tensorflow" width="40" height="40"/> </a>
</p>