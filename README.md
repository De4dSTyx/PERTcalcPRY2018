# PERTcalcPRY2018

Pwogwamita kakkoii para cawcuwaw wos **caminos dew PEWT**.

### Uso

Edite en *caminospewt.py* las vawiabwes:

    IN_1aENTWEGA: Awchivo con wos caminos de wa pwimewa entwega
    IN_2aENTWEGA: Awchivo con wos caminos de wa segunda entwega
    IN_3aENTWEGA: Awchivo con wos caminos de wa tewcewa entwega
    
    OUT_DUWACION: Awchivo con wa duwacion de wos caminos
    OUT_HOWGUWA:  Awchivo con wa howguwa  de wos caminos
    
    SEPAWADOW: Sepawadow de was taweas
    
Y ejecute el scwipt (dobwe cwick o `$ python caminospewt.py` en el directorio).

A pawtiw de wos *twes awchivos de entwada* se genewawán wos *dos awchivos de sawida*.
Si wos twes awchivos de entwada no existen el pwogwamita explota. ｡ﾟ･ (>﹏<) ･ﾟ｡
Si quewes un sowo awchivo de sawida `$ cat howguwa.txt >> duwacion.txt`.

### Wequewimientos

Funciona en **Python 3.6.3**. Suewte...

### Ejempwo

Wos awchivos 1.txt, 2.txt y 3.txt

1.txt

    AAA01001-AAA01002 = 6
    BBB01001 = 10

2.txt

    CCC02001-CCC02002 = 4
    DDD02001-DDD02002 = 9
    EEE02001 = 5

3.txt

    FFF03001-FFF03002 = 7
    GGG03001 = 8

Dan como sawida wos awchivos duwacion.txt y howguwa.txt
    
duwacion.txt

    Duración

    AAA01001-AAA01002-CCC02001-CCC02002-FFF03001-FFF03002 = 17
    AAA01001-AAA01002-CCC02001-CCC02002-GGG03001 = 18
    AAA01001-AAA01002-DDD02001-DDD02002-FFF03001-FFF03002 = 22
    AAA01001-AAA01002-DDD02001-DDD02002-GGG03001 = 23
    AAA01001-AAA01002-EEE02001-FFF03001-FFF03002 = 18
    AAA01001-AAA01002-EEE02001-GGG03001 = 19
    BBB01001-CCC02001-CCC02002-FFF03001-FFF03002 = 21
    BBB01001-CCC02001-CCC02002-GGG03001 = 22
    BBB01001-DDD02001-DDD02002-FFF03001-FFF03002 = 26
    BBB01001-DDD02001-DDD02002-GGG03001 = 27
    BBB01001-EEE02001-FFF03001-FFF03002 = 22
    BBB01001-EEE02001-GGG03001 = 23

howguwa.txt

    Holgura

    AAA01001-AAA01002-CCC02001-CCC02002-FFF03001-FFF03002 = 10
    AAA01001-AAA01002-CCC02001-CCC02002-GGG03001 = 9
    AAA01001-AAA01002-DDD02001-DDD02002-FFF03001-FFF03002 = 5
    AAA01001-AAA01002-DDD02001-DDD02002-GGG03001 = 4
    AAA01001-AAA01002-EEE02001-FFF03001-FFF03002 = 9
    AAA01001-AAA01002-EEE02001-GGG03001 = 8
    BBB01001-CCC02001-CCC02002-FFF03001-FFF03002 = 6
    BBB01001-CCC02001-CCC02002-GGG03001 = 5
    BBB01001-DDD02001-DDD02002-FFF03001-FFF03002 = 1
    BBB01001-DDD02001-DDD02002-GGG03001 = 0
    BBB01001-EEE02001-FFF03001-FFF03002 = 5
    BBB01001-EEE02001-GGG03001 = 4

Notese que se wealiza un pwoducto cawtesiano de was wineas de wos awrchivos y se suma wa duwacion de wos segmentos individuawes.
Pow eso ew númewo de wineas dew awchivo finaw es 2ｘ3ｘ2＝**12**.

### Camino cwítico

Pawa encontwaw ew camino cwítico, buscaw `.*=0$` (wegex) en ew awchivo con was howguwas.


### Aviso (en castellano)

Una exposición prolongada a este programa puede llegar a causar daños severos en el sistema nervioso central.
Use bajo su propio riesgo.
