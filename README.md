# bitsxLaMaratoProteines

## Inspiració
En el marc de **BitsXLaMarató** ja estem motivats a portar a terme projectes de caràcter solidari amb connotacions mèdiques. Nogensmenys, dels quatre reptes presentats, tres d'ells requerien de la creació d'aplicacions o similars, que és un aspecte de la informàtica que a la major part dels membres de l'equip ens sembla menys apassionant que no pas allò del que requeria el repte finalment escollit, que implica coneixements en HPC (_High Performance Computing_ o _Computació d'Altes Prestacions_ en català) i bioinformàtica. 

Tots dos camps ens resulten molt engrescadors al conjunt de l'equip, el primer perquè és el camp en el que treballem tots quatre (al BSC - Barcelona Supercomputing Center), i el segon perquè és un aspecte més aviat desconegut, del qual hem començat a conèixe'l els últims mesos per diverses raons i aquesta és una bona oportunitat per endinsar-nos-hi més.

Així doncs, el repte _Interacció de proteïnes. Ens fiquem d’acord?_ ens ha semblat el més adhient pels nostres interessos personals, i per aquest motiu l'hem escollit. 

## Què fa
Fonamentalment, des d'un punt de vista de computació algorítmica, utilitzant diferents algoritmes de communities sobre grafs no dirigits, traiem mètriques de les distpancies entre proteïnes. A més, hem paral·litzat aquest procés mitjançant COMPSs.

![Figura 1](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/769/589/datas/gallery.jpg)
![Figura 2](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/769/590/datas/gallery.jpg)
![Figura 3](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/769/591/datas/gallery.jpg)
![Figura 4](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/769/592/datas/gallery.jpg)

La modularitat és la fracció en que les arestes que cauen dels grups donats menys la fracció esperada si les arestes estiguessin distribuïdes a l'atzar.

## Com l'hem construït
Inicialment, un cop teníem les dades descomprimides, hem escrit un script de Python per calcular les distàncies entre les proteïnes _5FQD_, que corresponen al primer set de dades. Concretament, hem utilitzat les poses de l'output del ZDock, ja que és el que tenia un menor nombre de poses.

A continuació, en adonar-nos-en de l'enorme temps de còmput, hem optat per intentar paral·litzar l'script utilitzant COMPSs.

## Dificultats que ens hem trobat
En una primera instància, vam arribar a l'extrem d'estar a punt de tirar la tovallola en trobar-nos amb un obstacle majúscul que, aparentment, no ho hauria d'haver estat: per tal d'obtenir la informació dels PDBs calia descomprimir els fitxers XTC a fitxers PDB, però això se'ns va fer molt complicat, fins que després de molts intents, i de rebre l'ajuda de les dues organitzadores del projecte, vam aconseguir fer-ho.

Un cop podíem accedir bé a les dades, els fronts amb els que ens vam anar trobant eren de caràcter tècnic, a destacar el fet que els temps de còmput són increïblement elevats, i ens han obligat a fer mans i mànigues per encaixar-ho en els tempos de l'esdeveniment.

## Assoliments dels que estem orgullosos
Seguint en la línia del punt anterior, estem fortament orgullosos d'haver esquivat el primer obstacle, així com d'haver estat capaços d'haver aconseguit dades i de processar-les de forma satisfactòria.

A més, hem aconseguit fer una paral·lelització en fase molt inicial de desenvolupament d'un fragment de l'output de zdock, concretament del 1995 al 1999, fent només la matriu superior.

![Figura 5](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/769/549/datas/original.png)
![Figura 6](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/769/546/datas/gallery.jpg)
![Figura 7](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/769/547/datas/gallery.jpg)

## El que hem après
Fonamentalment, ens ha servit per assolir nous coneixements en el camp de la bioinformàtica i biologia en general, fruit de les primeres hores de recerca sobre del tema.

 També hem après a utilitzar COMPSs, un programming model desenvolupat al BSC, que un dels membres del nostre equip l'utilitza en el seu dia a dia laboral, i ens ha deleïtat explicant-nos-el.

![Figura 8](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/769/595/datas/gallery.jpg)

## Quin és el futur del projecte.
Es podria procedir en l'estudi de les dades intentant paral·lelitzar millor el procediment en el seu conjunt, ja que restringits pel temps només s'ha pogut fer una paral·lelització molt tímida.
