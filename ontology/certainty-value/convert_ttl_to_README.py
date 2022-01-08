
import sys

with open(sys.argv[1], 'r') as f:
    content = f.read()
prefixdict = {}
readme = open('README.md', 'w')
content = content.split('\n')
counter = 0
for line in content:
    if line.startswith('@prefix'):
        prefix = line[line.find('@prefix ')+8:line.find(':')]
        link = line[line.find('<')+1:line.find('>')]
        prefixdict[prefix] = link

prefixdict['rdf'] = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'

readme.write('# Ontology certainty-value\n\n')
readme.write('<div align="center"><img src="archiving.jpg" width="600"></div>\n\n')
for line in content:
    if line.startswith('# CLASSES') or line.startswith('# INSTANCES'):
        readme.write(line + '\n')   
    elif line.startswith('<'):
        readme.write('| Predicate | Object |\n|:-------- |:-------- |\n')
    elif line.startswith('@prefix') or line.startswith('@base') or line.startswith('#') or line.startswith('\t#') or line.startswith('    #') or line.startswith('    ') or line == '' or line == '\t' or line == ' ':
        pass
    elif line.startswith(sys.argv[1].replace('.ttl','')):
        readme.write('## ' + line.replace(sys.argv[1].replace('.ttl','')+':','')+'\n')
        readme.write('| Predicate | Object |\n|:-------- |:-------- |\n')
    else:
        line = line.replace('\t','')
        line = line.split(' ',1)
        if line[0].startswith('a'):
            line[0] = line[0].replace('a','rdf:type')
        pred = line[0].split(':')
        #Wenn Objekt = Link
        if line[1].find('"') == -1 and line[1].find('<') == -1:
            #Wenn mehrere Subklassen
            if line[0] == 'rdfs:subClassOf' and ', ' in line[1]:
                line[1] = line[1][:-1]
                objects = line[1].split(', ')
                multiObj = ""
                for ob in objects:
                    obj = ob.split(':')
                    obj = '[' + ob +']('+prefixdict[obj[0]] +obj[1]+')'
                    multiObj = multiObj + obj + ", "
                readme.write('| [' +line[0] +']('+prefixdict[pred[0]] +pred[1] +') | ' + multiObj[:-2] + '. |\n')
            else:
                obj = line[1].split(':')
                obj = '[' + line[1][:-1] +']('+prefixdict[obj[0]] +obj[1][:-1]+')' + line[1][len(line[1])-1:]
                readme.write('| [' +line[0] +']('+prefixdict[pred[0]] +pred[1] +') | ' + obj + ' |\n')

        #Wenn Objekt = String
        else:
            obj = line[1]
            readme.write('| [' +line[0] +']('+prefixdict[pred[0]] +pred[1] +') | ' + obj + ' |\n')

