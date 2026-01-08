FROM python:3.13
WORKDIR /Structured_Enquiry
COPY . .
RUN pip install --no-cache-dir pytest
RUN pytest -v
ENTRYPOINT ["python", "student.py"]
