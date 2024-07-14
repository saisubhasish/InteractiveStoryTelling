# Use an official Python runtime as a parent image
FROM python:3.12.0-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 for FastAPI and port 8501 for Streamlit
EXPOSE 8000
EXPOSE 8501

# Environment variables for Streamlit
ENV STREAMLIT_SERVER_PORT 8501
ENV STREAMLIT_SERVER_ENABLE_CORS false
ENV STREAMLIT_SERVER_HEADLESS true

# Command to run FastAPI server and Streamlit app
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & streamlit run app.py"]