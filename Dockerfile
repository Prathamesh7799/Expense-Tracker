FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN python3 webapp1.py

EXPOSE 8080

CMD ["streamlit", "run", "webapp1.py"]
