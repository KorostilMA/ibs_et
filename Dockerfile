FROM python
WORKDIR /ibs_et/
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["pytest",  "./test_suites/"]