import re
import random
import string
import streamlit as st # type: ignore

def check_password_strength(password):  

    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔴 Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔴 Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*()_+=]", password):
        score += 1
    else:
        feedback.append("🔴 Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score >= 5:
        return "🔥 Ultra Strong", "✅ Your password is ultra secure!", feedback
    elif score == 4:
        return "✅ Strong", "Your password is strong!", feedback
    elif score == 3:
        return "⚠️ Moderate", "Consider adding more security features.", feedback
    else:
        return "❌ Weak", "Your password is too weak. Improve it using the suggestions below.", feedback

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+="
    return ''.join(random.choice(characters) for _ in range(16))

# Streamlit UI Styling
st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")
st.markdown("""
    <style>
        .stApp { background-color: #ffc0cb; color: white; text-align: center; }
        .stTextInput input { border-radius: 8px; border: 2px solid #58a6ff; padding: 10px; }
        .stButton>button { background: linear-gradient(90deg, #58a6ff, #1f6feb); color: white; border-radius: 8px; font-weight: bold; }
        .password-box { font-size: 18px; font-weight: bold; color: #58a6ff; }
    </style>
""", unsafe_allow_html=True)

st.title("🔐 Stunning Password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if password:
    strength, message, suggestions = check_password_strength(password)
    
    st.subheader(f"Password Strength: {strength}")
    if "✅" in strength:
        st.success(message)
    else:
        st.warning(message)
    
    if suggestions:
        st.write("💡 Suggestions:")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")

if st.button("🚀 Generate Strong Password"):
    strong_password = generate_strong_password()
    st.markdown(f"<div class='password-box'>🔑 Suggested Strong Password: `{strong_password}`</div>", unsafe_allow_html=True)
