# Systemd

Ejemplo de reconfigurar servicio.

## Editar configuración

    sudo vim /etc/systemd/system/ollama.service

## Reload

    sudo systemctl daemon-reload

## Restart

    sudo systemctl restart ollama

## Logs

    journalctl -f -u ollama

