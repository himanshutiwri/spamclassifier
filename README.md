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
   -then in settings :![image](<"https://github.com/user-attachments/assets/dfca04d9-8654-431c-8d84-0df9e1a43196")


6. **So click on manual Deploy and select deploy with latest commit**
   -and wait 2-3 mint after that your website will be published.
   -https://spam-classifier-d15y.onrender.com/

   ![image](<"https://github.com/user-attachments/assets/9e40871d-f6d6-48b1-8458-ba9dc774ac9c")

   The output:
   ![image](<"https://github.com/user-attachments/assets/64da89ae-8996-4ef4-a5f7-65e46bc82958")


   
🙌 Conclusion

This project demonstrates Text Classification using ML + NLP with Flask deployment.

