# Depurando con ddev, vim y vdebug

## Activar depuarción

ddev xdebug

## vdebug en vim

https://github.com/vim-vdebug/vdebug

### Configuración de vdebug en .vimrc

```
Plugin 'vim-vdebug/vdebug'
let g:vdebug_options = {}
let g:vdebug_options.port = 9003
let g:vdebug_options.path_maps = {'/var/www/html': getcwd()}
```

### Añadir breakpoint

<F10>


### Iniciar depurador

<F5>

## Teclas por defecto.

- <F5>: start/run (to next breakpoint/end of script)
- <F2>: step over
- <F3>: step into
- <F4>: step out
- <F6>: stop debugging (kills script)
- <F7>: detach script from debugger
- <F9>: run to cursor
- <F10>: toggle line breakpoint
- <F11>: show context variables (e.g. after "eval")
- <F12>: evaluate variable under cursor
- :Breakpoint <type> <args>: set a breakpoint of any type (see :help VdebugBreakpoints)
- :VdebugEval <code>: evaluate some code and display the result
- <Leader>e: evaluate the expression under visual highlight and display the result


