import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file,get_file
import google.generativeai as genai
import time
from pathlib import Path
import tempfile
from dotenv import load_dotenv
load_dotenv()
import os


# Page Configuration
st.set_page_config(
    page_title="Multimodel AI Agent - Video Summarizer",
    page_icon="🎥",
    layout="wide"
)
st.title("Phidata Multimodel AI Agent")
st.header("Powered by Gemini 2.0 Flash Exp")

@st.cache_resource
def initialize_agent():
    return Agent(
        name ="Video AI summarizer",
        model = Gemini(id="gemini-1.5-flash"),
        tools = [DuckDuckGo()],
        markdown = True
    )

# Initialize the agent
multimodel_agent = initialize_agent()

video_file = st.file_uploader(
    "upload a video file", type=['mp4','mov','MPEG-4 movie'], help="upload a video for Ai analysis"
)

if video_file:
    with tempfile.NamedTemporaryFile(delete=False,suffix='.mp4') as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name
    
    st.video(video_path,format="video/mp4",start_time=0)

    user_query = st.text_area(
        "what insights are you seeking form the video?",
        placeholder="Ask anything about the video content, The AI agent will analyze and gather additional information.",
        help ="provide specific questions or insghts you want from the video."

    )

    if st.button("Analyze video", key="analyze_video_button"):
        if not user_query:
            st.warning("Please enter a question or insight to analyze the video")
        else:
            try:
                with st.spinner("Analyzing video..."):

                    model = genai.GenerativeModel("gemini-1.5-flash")

                    with open(video_path, "rb") as f:
                        video_data = f.read()

                    response = model.generate_content([
                        user_query,
                        {
                        "mime_type": "video/mp4",
                        "data": video_data
                    }
                ])

                st.subheader("Result")
                st.markdown(response.text)

            except Exception as error:
                st.error(f"An error occurred during analysis: {error}")

            finally:
                Path(video_path).unlink(missing_ok=True)
    else:
        st.info("Upload a video file to begin analysis")
