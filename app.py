import streamlit as st
import json
from friends_recomemnder_module import people_you_may_know
from pages_recomender import Pages_might_like_by_user

# Load data
def data_load(filename):
    with open(filename, "r") as f:
        return json.load(f)

data = data_load("massive_data.txt")

st.title("🤝 Friends & Pages Recommendation App")

user_id = st.number_input("Enter your User ID:", min_value=1, step=1)

if st.button("Get Recommendations"):
    st.subheader("👥 People You May Know")
    friends = people_you_may_know(user_id, data)
    if friends:
        for uid, count in friends:
            st.write(f"User ID {uid} — {count} mutual friend(s)")
    else:
        st.write("No suggestions found or invalid user ID.")

    st.subheader("📄 Pages You Might Like")
    pages = Pages_might_like_by_user(user_id, data)
    if pages:
        for page_id, score in pages:
            st.write(f"Page ID {page_id} — Score: {score}")
    else:
        st.write("No page suggestions found.")
