FROM python:3.11
WORKDIR /student
COPY . .
CMD ["python", "student.py"]