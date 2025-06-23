# 🤝 Friends & Pages Recommendation App

This is a mini recommendation system built using **Python** and **Streamlit**, which suggests:
- 👥 **People You May Know** – based on mutual friends
- 📄 **Pages You Might Like** – based on shared liked pages

It simulates a small-scale social network to provide intelligent suggestions just like Facebook or LinkedIn.

---

## 📂 Folder Structure

```
Friends_and_Pages_Recommender_App/
├── app.py                     # Streamlit user interface
├── friends_recommender_module.py  # Logic to suggest friends
├── pages_recommender.py       # Logic to suggest pages
├── massive_data.txt           # Sample user + page dataset
├── requirements.txt           # All necessary Python libraries
└── README.md                  # Project documentation (this file)
```

---

## ▶️ How to Run

Make sure Python and pip are installed. Then:

```bash
pip install -r requirements.txt
streamlit run app.py
```

⏩ The app will open in your browser (usually at http://localhost:8501)

---

## 👤 Try with Sample User IDs:

Some IDs you can test with:
```
User ID: 1
User ID: 2
User ID: 10
```

---

## 🧠 How It Works

### 1. Friend Recommendation:
- Finds direct friends of the user
- Then checks mutual friends from those connections
- Suggests users with highest number of mutual friends

### 2. Page Recommendation:
- Finds pages liked by user
- Then looks at pages liked by other users with similar page interests
- Scores pages based on overlap, and recommends highest scored pages

---

## 💻 Tech Stack

- **Python**
- **Streamlit** – for frontend
- **JSON** – for sample dataset
- **Modular Code Structure**

---

## 📸 Screenshots

### 👥 Friend Suggestions
![Friend Suggestion](screenshots/friend_suggestion.png)

### 📄 Page Suggestions
![Page Suggestion](screenshots/page_suggestion.png)

---

## 📘 Sample Dataset

`massive_data.txt` contains users like:
```json
{
  "users": [
    {
      "id": 1,
      "name": "Alice",
      "friends": [2, 3],
      "liked_pages": [101, 102]
    },
    ...
  ]
}
```

---

## 🌐 Future Improvements
- Add user login + database (SQLite/Mongo)
- Show profile names, not just IDs
- Deploy online using **Streamlit Cloud** or **Render**

---

## 🙋‍♂️ Author

**Sachin / Kiran (You can update this)**  
📧 Contact: your_email@example.com  
🌐 GitHub: [github.com/yourusername](https://github.com/yourusername)

---

## 📄 License
This project is open-source and free to use under the MIT License.