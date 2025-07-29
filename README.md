# 🗽 NYC Restaurant Inspection Risk Classification

This **README.md** helps setting up the project and also have some extra notes that can be helpfull for running this project.


## Project Setup

1. **Make sure you are in the project directory**

2. **Make sure you have uv in your pc**
    * For Mac:
    ```bash
   brew install uv
   ````

    * For Windows:


3. **Install and add project dependencies**

    * Install:
        ```bash
        uv sync
       ````
    * Add:
       ```bash
       uv add <package name>
       ````

4. **Activate virtual environment**
    ```bash
    source .venv/bin/activate
    ````

5. **Select the correct Jupyter kernel**
When you launch Jupyter and select the kernel to start working, it should be the environment you just created.


## Other important notes

1. **LLM SetUp**

To enable Large Language Model (LLM) functionality (e.g., for generating `violation_category` and for the extra analysis), you'll need to set up your API key for Mistral.

1. Create a `.env` file in the root of your project directory.
2. Add your **Mistral API key** to the file as follows:

   ```env
   MISTRAL_API_KEY=<API_KEY_TOKEN>
   ```

Note: For privaty reasons, the API key is not included in this repository.


## Project structure

<pre><code>.
├── data
│   └── data.csv
├── final_notebook
│   └── main.ipynb
├── pyproject.toml
├── README.md
├── src
│   ├── config.py
│   ├── llm_call.py
│   ├── model.py
│   ├── plots.py
│   └── utils.py
└── uv.lock
</code></pre>

For the notebook to have a lot of extra information I added a lot of code in different scripts located on the `src` folder.

To run the code is just select the kernel on the notebook `main.ipynb` located on `final_notebook`folder and run each sell, after all the setup.