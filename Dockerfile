FROM python:3.12
WORKDIR /app
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
