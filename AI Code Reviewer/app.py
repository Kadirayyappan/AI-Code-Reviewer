import streamlit as st
import google.generativeai as genai

# Configure your Google API key
genai.configure(api_key="AIzaSyCr-VJjpv4UnFuwVbfoeJnrPeBPKgcL3pY")  # Updated API key

# Advanced Sidebar (Bio Section + Connect with Me)
with st.sidebar:
    # Connect with Me Section (Logos)
    st.title("Connect with Me")
    st.markdown("""<a href="https://www.linkedin.com/in/kadir-ayyappan2005" target="_blank">
        <img src="https://th.bing.com/th/id/OIP.b5oDvUVU5UVN4cefTJGq3wHaHa?w=196&h=196&c=7&r=0&o=5&dpr=1.3&pid=1.7" alt="LinkedIn" width="40" height="40"/>
    </a>
    &nbsp;
    <a href="https://github.com/Kadirayyappan" target="_blank">
        <img src="https://th.bing.com/th/id/OIP.eoZPB2gfGH-1ckaL_JSZdwHaHg?w=158&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" alt="GitHub" width="40" height="40"/>
    </a>
    """, unsafe_allow_html=True)

    # Add a gap between the image and the title using CSS margin
    st.markdown("<div class='image-gap'></div>", unsafe_allow_html=True)
    st.image("R.png", use_container_width=True)
    
    # Updated Sidebar Content
    st.markdown("""
    ### Internship at:  
    **Innomatics Research Labs**  
    Supervised by: **Kanav Bansal**  
    ---
    **Project Overview**:  
    This AI-powered tool is designed to help you improve Python code by offering:  
    - Bug detection  
    - Suggestions for better practices  
    - Fixed code snippets  
    ---
    **Key Features**:  
    - **Instant AI Code Review**  
    - **Interactive Chat History**  
    - **Simple & Clean User Interface**  
    - **Real-time Code Analysis**  
    ---
    ### Developer's Insight:
    This tool was created as part of an internship to explore AI-assisted code review capabilities, helping developers write better code with less effort.
    """)

# Main Interface
# Animated title on the main page
st.markdown("<h1 class='animated-title'>GenAI Code Reviewer</h1>", unsafe_allow_html=True)
st.markdown("**Simply paste your Python code below and get real-time feedback!**")

llm = genai.GenerativeModel("models/gemini-1.5-flash")
chatbot = llm.start_chat(history=[])

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

def update_chat(role, message):
    st.session_state["chat_history"].append({"role": role, "content": message})

input_code = st.text_area("Paste your Python code here:", height=200)

# Button for code review
if st.button("Review Code"):
    if input_code.strip():
        update_chat("human", input_code)
        review_prompt = f"Review the following Python code. Identify bugs, areas of improvement, and provide fixed code snippets:\n{input_code}"
        response = chatbot.send_message(review_prompt)
        
        # Add AI response to chat history and display
        update_chat("ai", response.text)
        st.success("Code reviewed successfully! Here are the suggestions:")
        st.subheader("AI's Suggestions & Fixes:")
        st.write(response.text)
    else:
        st.warning("Please paste some Python code to review.")

# Button to view past history
if st.button("Show Review History"):
    if st.session_state["chat_history"]:
        st.subheader("Review History")
        for entry in st.session_state["chat_history"]:
            role = "User" if entry["role"] == "human" else "AI"
            st.markdown(f"**{role}:** {entry['content']}")
    else:
        st.info("No review history available yet.")

# Additional Styling for a Clean UI
st.markdown("""
    <style>
        /* Text Animation for Title */
        @keyframes typing {
            from {
                width: 0;
            }
            to {
                width: 100%;
            }
        }

        .animated-title {
            font-family: 'Courier New', monospace;
            font-size: 4em;
            color: #f39c12;  /* Lighter, vibrant title color */
            white-space: nowrap;
            overflow: hidden;
            border-right: 3px solid #e74c3c;
            width: 0;
            animation: typing 4s steps(40) 1s 1 normal both;
        }

        .stTextInput>div>div>input {
            border-radius: 12px;
            background-color: #f7f7f7;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stSuccess>div>div {
            background-color: #e0ffe0;
        }
        .stWarning>div>div {
            background-color: #fff4e5;
        }

        /* CSS for Image Gap */
        .image-gap {
            margin-bottom: 20px; /* Adjust the gap size */
        }

        /* Animation for Flying Balloons */
        @keyframes flyBalloon {
            0% {
                transform: translateY(100vh) translateX(0) rotate(0deg);
                opacity: 1;
            }
            100% {
                transform: translateY(-100vh) translateX(50vw) rotate(360deg);
                opacity: 0;
            }
        }

        .balloon {
            position: fixed;
            bottom: 0;
            left: 50%;
            width: 50px;
            height: 80px;
            background-color: #ff3366;
            border-radius: 50%;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
            animation: flyBalloon 8s infinite ease-in-out;
        }

        .balloon:nth-child(2) {
            background-color: #ff6600;
            animation-delay: 2s;
        }

        .balloon:nth-child(3) {
            background-color: #3399ff;
            animation-delay: 4s;
        }

        .balloon:nth-child(4) {
            background-color: #33cc33;
            animation-delay: 6s;
        }
    </style>
""", unsafe_allow_html=True)

# Add balloons to the page with animation
st.markdown(""" 
    <div class="balloon"></div>
    <div class="balloon"></div>
    <div class="balloon"></div>
    <div class="balloon"></div>
""", unsafe_allow_html=True)
