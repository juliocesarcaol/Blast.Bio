from Bio.Blast.Applications import NcbiblastnCommandline
from Bio import SeqIO

from flask import Flask, request
import xmltodict, json



app = Flask(__name__)

## Crear query fasta file
def create_file(query_sequence, query_id):
    with open('query.fasta', 'w') as file:
        file.write('>')
        file.write(query_id)
        file.write("\n")
        file.write(query_sequence)
        file.write("\n")

## Ejecuta BLAST con tres parametros query, db & seq_record. El resultado es un xml que se pasa json para ser leido por postgres luego
def blast_search(query_sequence, query_id):

    create_file(query_sequence, query_id)

    # Ruta al archivo de secuencia en formato FASTA
    seq_file = "query.fasta"

    # Ruta al archivo de base de datos BLAST en formato FASTA
    db_file = "out.fas"

    # Leer la secuencia desde el archivo FASTA
    seq_record = SeqIO.read(seq_file, format="fasta")
    print("record: %s" % seq_record)



    # Crear la línea de comando para blastp
    #blastn_cline = NcbiblastnCommandline(blastn_path, query=seq_file, db=db_file)

    blastn_cline = NcbiblastnCommandline(query = "query.fasta", db = "out.fas", 
    outfmt = 5, out = "results.xml") 
    stdout, stderr = blastn_cline()
    resultado = ""
    with open("results.xml", "r") as results_handle:
        resultado = results_handle.read()
    return resultado

# XML a JSON 
def blast_search_json(query_sequence, query_id):
    o = xmltodict.parse(blast_search(query_sequence, query_id))
    print(o)
    return json.dumps(o)

#devuelve el resultado de esta aplicaci'on a postGRES 
@app.route('/blast/search', methods=['POST'])
def blast_search_endpoint():
    # Obtén la secuencia de consulta del cuerpo de la solicitudn
    data = request.get_json()
    query_sequence = data['query_sequence']
    query_id = data['query_id']
    print(query_id)
    print(query_sequence)
    #query_sequence = "ABD"
    # Realiza la búsqueda Blast utilizando la función anterior
    results = blast_search_json(query_sequence, query_id)

    # Devuelve los resultados de la búsqueda como respuesta HTTP
    #return jsonify(results)
    return results


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
