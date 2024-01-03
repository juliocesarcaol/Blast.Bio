import xmltodict
file=open("_select_organisms_catalog_number_gen_taxa_name_sequence_from_org_202310161650.xml","r")
file1 = open('out.fasta', 'w')
xml_string=file.read()
print("The XML string is:")
#print(xml_string)
python_dict=xmltodict.parse(xml_string)
print("The dictionary created from XML is:")
#print(python_dict)
#for key in python_dict:
#    print(key, "->", python_dict[key])
claves_ya_agregadas = []
seen = set()


for rowfas in python_dict['dataset']['SELECT_ORGANISMS_CATALOG_NUMBER_GEN_TAXA_NAME_SEQUENCE_FROM_ORGANISM_SEQUENCES_INNER_JOIN_ORGANISMS_ON_ORGANISMS_ID_ORGANISM_ID_INNER_JOIN_TAXA_ON_TAXA_ID_ORGANISMS_TAXON_ID_INNER_JOIN_TAXON_TYPES_ON_TAXON_TYPES_ID_TAXON_TYPE_ID']:
    print(rowfas['@CATALOG_NUMBER'])
    clave = rowfas['@CATALOG_NUMBER'] + "_" + rowfas['@GEN'] + "_" + rowfas['@NAME']
    clave = clave.replace(" ", "_")
    clave = clave.replace("(", "_")
    clave = clave.replace(")", "_")
    clave = clave.replace("{\*\expandedcolortbl;;}","")
    clave = clave.replace("\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0","")
    clave = clave.replace("{\fonttbl\f0\fswiss\fcharset0Helvetica;}","")
    clave = clave.upper()
    clave = clave.replace("[NULL]","nogen")
    clave = clave[0:49]
    sequence = rowfas['@SEQUENCE']
    sequence = sequence.replace("-","")
    sequence = sequence.replace("?","")
    sequence = sequence.replace(" ","")
    if clave not in seen:
        file1.write(">" + clave + "\n")
        file1.write(sequence + "\n")
        seen.add(clave)
        claves_ya_agregadas.append(clave)

file1.close()
file.close()