
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

readme.write('# Ontology archiving\n')
for line in content:
    if line.startswith('# CLASSES') or line.startswith('# PROPERTIES'):
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
        prop = line[0].split(':')
        if line[1].find('"') == -1 and line[1].find('<') == -1:
            obj = line[1].split(':')
            obj = '[' + line[1][:-1] +']('+prefixdict[obj[0]] +obj[1][:-1]+')' + line[1][len(line[1])-1:]
        else:
            obj = line[1]
        readme.write('| [' +line[0] +']('+prefixdict[prop[0]] +prop[1] +') | ' +obj + ' |\n')

