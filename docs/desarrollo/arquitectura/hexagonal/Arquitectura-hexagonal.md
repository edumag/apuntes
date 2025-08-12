# Arquitectura hexagonal

## Estructura de directorios

```
src/
  - apps/
    - <Aplicación>/
      - config/
      - controllers/
      - utils/
      start.ts
      <Aplicación>App.ts
  - Contexts/
    - <Aplicación>/
      - application/
      - domain/
      - infrastructure/
    - Shared/
      - application/
      - domain/
      - infrastructure/
```
