# Step 1: Base image
FROM python:3.10-slim

# Step 2: Set up the working directory
WORKDIR /app

# Step 3: Copy project files to the container
COPY . /app

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose any required ports (for dashboard, if applicable)
EXPOSE 8501

# Step 6: Define the default command (optional, depending on use case)
CMD ["python", "scripts/data_pipeline.py"]
