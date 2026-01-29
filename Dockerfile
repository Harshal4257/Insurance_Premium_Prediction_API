# Base Image
FROM python:3.11-slim

#Set Working Directory
WORKDIR /app

#Copy the requiremets.txt
COPY requirements.txt .

#Install the libraries
RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest application code
COPY . .

#Expose the port
EXPOSE 8000

#Run the application
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]
