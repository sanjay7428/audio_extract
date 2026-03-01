FROM python:3.11-slim

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Railway provides PORT automatically
ENV PORT=8000

# Start using Railway dynamic port
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT}
