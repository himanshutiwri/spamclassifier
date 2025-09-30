# SmS_Spam_Classifier

A **web application** that predicts whether a message is **Spam** or **Not Spam** using **Machine Learning** and **Natural Language Processing**.  

Built with **Python**, **Flask**, **NLTK**, and **Scikit-learn**.  

1. **Setup Virtual Environment**:
   - Open the terminal.
   - Install the virtual environment package if you haven't already: `conda create -p venv python=3.9 -y`.
   - Create a virtual environment: `virtualenv venv`.
   - Activate the virtual environment:
    conda activate venv/

    # Using conda  
conda create -p venv python=3.9 -y  
conda activate venv/

# OR using virtualenv  
pip install virtualenv  
virtualenv venv  
venv\Scripts\activate   # (Windows)  
source venv/bin/activate  # (Linux/Mac)



2. **Install Requirements**:
   - Install the requirements: `pip install -r requirements.txt`.

3. **Set Up the Jupyter Notebook**:
   - Open the Jupyter Notebook in your virtual environment.
   - pip install ipykernel
   - pip install jupyter notebook

4. **Run Application.py**:
   -python app.py
   Then open the browser at http://127.0.0.1:5000/

5. **Let's Deploy it at Render.com**:
   -go to this website: https://dashboard.render.com/web
   -then click on new and choose web serivces
   -choose this :Build and deploy from a Git repository and click on next
   -then in settings :image can be seen in screenshot folder [Screenshot 1](screenshot/Screenshot_2025-09-27_113600.png)


6. **So click on manual Deploy and select deploy with latest commit**
   -and wait 2-3 mint after that your website will be published.
   -https://spamclassifier-qozp.onrender.com/

[Screenshot 2](screenshot/Screenshot_2025-09-27_114322.png)

The output:
[Screenshot 3](screenshot/Screenshot_2025-09-27_145716.png)


   
🙌 Conclusion

This project demonstrates Text Classification using ML + NLP with Flask deployment.

