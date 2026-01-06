FROM python:3.11
WORKDIR /Structured_Enquiry
COPY . .
RUN pip install pytest
CMD ["python", "student.py"]