FROM ubuntu
LABEL maintainer "julio.cesar@"

RUN apt-get update && apt-get install -y \
    parallel \
    python3 \
    python3-pip \
    libidn11-dev \
    wget



RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.14.1/ncbi-blast-2.14.1+-x64-linux.tar.gz && \
    tar xzf ncbi-blast-2.14.1+-x64-linux.tar.gz

ENV PATH=".:/ncbi-blast-2.14.1+/bin:${PATH}"

RUN mkdir /query && mkdir /db && mkdir /out

RUN adduser --disabled-password --gecos '' dockeruser

RUN chown -R dockeruser /out

RUN pip3 install biopython
RUN pip3 install flask xmltodict


COPY p4.py /
COPY p5.py /

COPY query.fasta /
COPY out.fas /
COPY server.sh /
RUN chmod 777 server.sh

RUN pip3 install flask xmltodict

CMD '/server.sh'
 