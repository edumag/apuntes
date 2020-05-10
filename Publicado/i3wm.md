"=========== Meta ============
"StrID : 1277
"Title : I3wm Escritorio ligero
"Slug  : i3wm-escritorio-ligero
"Cats  : Linux
"Tags  : 
"=============================
"EditType   : post
"EditFormat : MD
"BlogAddr   : https://lesolivex.com
"========== Content ==========
# Personalización i3wm

## Instalación

```bash
# Instalamos dependencias.
sudo apt-get install i3 dunst compton tilix feh rofi

# Bajamos configuración.
git clone git@gitlab.com:edumag/i3-configuraci-n.git
mv i3-configuraci-n.git $HOME/.config/i3

# Instalamos font awesome.
wget https://github.com/creationix/boxcode/raw/master/font/fontawesome-webfont.ttf
[[ -d "$HOME/.fonts" ]] || mkdir $HOME/.fonts
mv fontawesome-webfont.ttf $HOME/.fonts/

# Fuente System San Francisco
wget https://github.com/supermarin/YosemiteSanFranciscoFont/blob/master/System%20San%20Francisco%20Display%20Regular.ttf?raw=true -o "$HOME/.fonts/System San Francisco Display Regular.ttf"

# Añadimos configuración propia a dunst
ln -s "$HOME/.config/i3/dunst" "$HOME/.config"

# Control de volumen
sudo apt-get install pasystray lxappareance pavucontrol
```



## Combinación de teclas básica

| Combinación      | Acción                                      |
| ---------------- | ------------------------------------------- |
| Mod+Enter        | Terminal                                    |
| Mod+Shift+Q      | Cerrar centana                              |
| Mod+d            | Lanzador aplicaciones                       |
| Mod+Shift+Space  | Cambiar ventana a modo flotante             |
| Mod+r            | Redimensionar ventana                       |
| Mod+Alt_L        | Seleccionar ventana con Rofi                |
| Mod+Shift+Flecha | Mover ventana de posición                   |
| Mod+w            | Cambio de disposición de ventanas (Layouts) |
| Mod+Flecha       | Cambiamos foco de ventana                   |
| Mod+f            | FullScreen                                  |
## font-awesome

[Font Awesome Free's Cheatsheet](https://fontawesome.com/cheatsheet?from=io)

Desde la web de fontawesome podemos copiar y pegar los iconos en nuestros
ficheros de configuración

## Rofi

Instalamos rofi como lanzador de aplicación
y de paso tenemos calculadora y selector de
ventanas.

### Menú de aplicaciones (Mod+d)

![Rofi1](https://gitlab.com/edumag/i3-configuraci-n/-/raw/master/img/i3wm-02.png)

### Calculadora (Mod+c)

![Rofi2](https://gitlab.com/edumag/i3-configuraci-n/-/raw/master/img/i3wm-03.png)

### Seleccionar ventana. (Mod+Tab_L)

![Rofi3](https://gitlab.com/edumag/i3-configuraci-n/-/raw/master/img/i3wm-04.png)

## dunst (Notificaciones)

![Rofi3](https://gitlab.com/edumag/i3-configuraci-n/-/raw/master/img/i3wm-05.png)

## pasystray (Volumen)

Al lanzar pasystray el icono oscuro no se ve bien.
Lanzamos lxappareance para cambiar el tema gtk y los iconos.

![Rofi3](https://gitlab.com/edumag/i3-configuraci-n/-/raw/master/img/i3wm-06.png)

## Configuración de touchpad.

```
sudo mkdir -p /etc/X11/xorg.conf.d && sudo tee <<'EOF' /etc/X11/xorg.conf.d/90-touchpad.conf 1> /dev/null
Section "InputClass"
        Identifier "touchpad"
        MatchIsTouchpad "on"
        Driver "libinput"
        Option "Tapping" "on"
EndSection

EOF
```
### Referencias

- https://cravencode.com/post/essentials/enable-tap-to-click-in-i3wm/

## Control de brillo

No he podido encontrar ninguna aplicación que me funcione, al final he realizado un simple script que hace la función.

> $ ./brightness.sh -h
>
> uso: brightness.sh [+|-]

## Referencias

- [Una buena explicación de como funciona](https://github.com/bookercodes/dotfiles.git)
- https://sergioquijanorey.github.io/i3/linux/programacion/administracion/2018/09/09/configuraci%C3%B3n-i3wm.html



