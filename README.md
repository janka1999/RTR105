# RTR105
Datormācības kursā elektroniskā kladē  

**1. Linux startēšana**  

Ieslēdzot linux operētājsistēmu atver terminālu ar kombinācuju: **_ctrl+alt+t_**  
Lai izveidu jaunu termināla cilni, kura atvieglo darbu terminālā jonospiež kombinācija: **_ctrl+shift+t_**  
Lai sakārtotu termināli jānospiež: **_ctrl+l_**  

**2. Darbs ar terminālu**   

*uname* - sistēma nosauc operētājsistēmu  
*man ....* - pievienojot jautājumam datorā, sniedz paskaidrojumus  
*man uname* - sistēma paskaidro funkciju un parāda papildus funkcijas  
*uname -a* - dod padziļunātu informāciju par operētājsistēmu  
*echo $0* - paziņo kādā valodā notiek procesi datorā  
*whoami* - parāda, kas lieto datoru  
*who* - parāda kad lietotājs ir ieslēdzis operētājsistēmu 
*ls* - parāda visas **redzamās** mapes un funkcijas konkrētajā atrašanās vietā  
*ls -l* - parāda lietotāju atļaujas konkrētajās mapēs vai failos  
*ls -a* - parāda **pilnīgi visus** failus un mapes datorā ar visām lietotāja atļaujām. Redzamās mapes ir zilā krāsā, bet slēptās melnā krāsā. Funkcijas apzīmē priekšā pieliekot **.**  
*history* - sniedz lietotājam atskaiti par veiktajiem procesiem pēc datora ieslēgšanas brīža. Labot šos datus var tikai administrators ar īpašu atļauju

**Darbības ar Linux terminālu 2**  

*cd* - atrašanās vietas maiņa sistēmā  
*pwd* - pēc pieprasījuma sistēma parāda konkrēto atrašanās vietu  
*cd ..* - maina atrašanās vietu uz augstāku  
*mkdir* - jaunas mapes izveide  
*rmdir* - mapes dzēšana  
*rm -r* - mapes dzēšana kopā ar apakšmapi  
*echo ""* - jebkāda teksta ievade terminālā  
*echo -e ""* - teksta ievade vertikāli atdalot vārdus ar /  
*echo "" > fails.txt* - teksta ievade konkrētā teksta dokumentā  
*chmod* - dokumenta ierobežojumu noteukšana  
*nano fails.txt* - brīvā teksta rakstīšanas forma konkrētā dokumentā(fails.txt)  
*mv fails.txt* - pārvietot dokumentu ar nosaukumu fails.txt  
*cp fails.txt* - izveidot dublikātu dokumentam fails.txt  
*mv fails*.txt /Musik - pārvietot visus dokumentus ar sākuma vārdu fails uz mapi Musik  
**=** labās puses informāciju piešķir kreisajai pusei  
*python* - jauna rakstīšanas vide
*ipython* - papildinātā versija python
*idle &* - cita rakstīšanas vide
*print(...)* - informācijas izvade
*vars()* - parāda informāciju vidē (arī mainīgos)

