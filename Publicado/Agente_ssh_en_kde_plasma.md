Afegim script d'inici: ~/.config/autostart-scripts/ssh-unlock.sh

[bash]
#!/bin/sh
export SSH_ASKPASS=/usr/bin/ksshaskpass
/usr/bin/ssh-add $HOME/.ssh/id_rsa </dev/null
[/bash]

Executem l'script per primera vegada:

[bash]
sh ~/.config/autostart-scripts/ssh-unlock.sh
[/bash]

Ens demanarà el password de la clau i podem especificar que no volem que
ens torni a preguntar.

D'aquesta manera ja podem treballar sense que ens pregunti cada vegada que la
utilitzem.
