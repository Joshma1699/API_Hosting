# 1. Use the official Python 3.10 image as the base
FROM python:3.10

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy all files from 'backend' to '/app' in the container
COPY . .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose port 8080 for Flask
EXPOSE 8080

# 6. Run the Flask app
CMD ["python", "apicreation.py"]
