
## Install and use (DEV)
Check that venv is installed.  
Then create a venv : `python3 -m venv venv`  
activate it : `source venv/bin/activate` (`venv\Scripts\activate.bat` on Windows)  
and install dependencies : `python -m pip install -r requirements.txt`

You are ready to go !

Nex times, `source venv/bin/activate` will do the job.

## Goals (de)

* Verschlüsseln/entschlüsseln
* Cracking
* Reach 136.06 Mbits/sec throughput

># Angriff gegen eine symmetrische Chiffre

>In dem Paper

>[A New Symmetric Key Encryption Algorithm Using Images as Secret Keys](https://ieeexplore.ieee.org/document/7420966)

>schlagen Mazhar Islam, Mohsin Shah, Zakir Khan, Toqeer Mahmood, Muhammad Jamil Khan auf der 13th International Conference on Frontiers of Information Technology (FIT15) ein symmetrisches Kryptoverfahren vor, das schneller als AES funktioniert.

>Wir wollen in diesem Projekt folgende Aufgaben rekonstruieren:
>* Implementieren Sie dieses Verfahren effizient. Versuchen Sie, effizienter zu sein als die angegebenen 136 MB/sec.
>* Knacken Sie dieses Verfahren mit einer Häufigkeitsanalyse.
>* Rekonstruieren Sie evtl. das verwendete Bild.

>## Vorstufe zur Attacke

>Implementieren Sie eine simple Substitutionschiffre.

>D.h. das Alphabet wird in einer beliebigen Permutation angegeben, beispielsweise
```
Key abcdefghijklmnopqrstuvwxyzäöü
    geiqouxdyväzfwlnhtbjpasmkörcü
```
>Der Text "Das ist ein Test." wird dann substituiert durch "Qgb ybj oyw Jobj."

>Wenn die Texte lang genug sind, kann dies durch Häufigkeitsanalyse mühelos automatisiert gebrochen werden. Am häufigsten etwa wird in einem verschlüsselten Text das "o" auftreten, weil der Buchstabe "e" im Klartext am häufigsten vorkommt.

>Schreiben Sie ein Programm, das auf diese Weise automatisiert den Klartext errät.

>## Attackieren des gegebenen Verfahrens

>Durch das verwendete Bild wird "e" durch verschiedene Werte verschlüsselt. Ist der Text lang genug, kommt es trotzdem zu einem gehäufteren Auftreten aller möglichen Werte einer Verschlüsselung (coordinate values) von "e".

>Stellen Sie experimentell fest, wieviel Chiffretext Sie in Abhängigkeit der Länge des Bildes benötigen, um den Klartext automatisiert zu ermitteln.
