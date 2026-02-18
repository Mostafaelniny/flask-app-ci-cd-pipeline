# Use an official Python runtime as a parent image
FROM python 


# Set the working directory in the container
WORKDIR /app


# Copy the requirements into the container at /app
COPY requirements.txt .


# Install dependencies from the requirements.txt file
RUN pip install -r requirements.txt


# Copy the source code into the container at /app
COPY app.py  .


# Install dependencies from the requirements.txt file
EXPOSE 5000


# Run the Flask app
CMD python app.py
