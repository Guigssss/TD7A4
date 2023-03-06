Dasn ce TD nous avons vu comment réaliser un bind mounts avec Docker et Docker Compose

Pour la partie withoutcompose :
- On se place dans le répertoire withoutcompose avec la commande 'cd withoutcompose'
- On build le container en luia ttribuant le tag "withoutcompose" à l'aide de la commande 'docker build -t "withoutcompose"'
- Je run mon container en lui attribuant le nom "withoutcompose", en mappant le port xxxx sur le port XXXX de ma machine, et en prenant le contenu de mon fichier.txt pour le mettre dans le file.txt du containeur et le -d pour ne pas avoir les logs dans le termianl. Cela se fait à l'aide de la commande 'docker run -d --name withoutcompose -p XXXX:xxxx -v mon\chemin\du\fichier.txt:/app/file.txt withoucompose'

Pour la partie withcompose :
- On se place dans le répertoire withcompose avec la commande 'cd withcompose'
- Je modifie dans le docker-compose.yml les chemins et ports de la même façon que dans la partie précédente
- Je lance mon container avec la commande 'docker-compose up'
