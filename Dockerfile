FROM ollama/ollama:latest

# Install Python + streamlit
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install streamlit ollama

# Copy the app
COPY app.py .

EXPOSE 8080

CMD ["sh", "-c", "ollama serve & sleep 5 && ollama pull deepseek-coder-v2:16b && streamlit run app.py --server.port=8080 --server.address=0.0.0.0"]
