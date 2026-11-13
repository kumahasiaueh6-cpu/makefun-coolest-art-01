# Coolest Art — make.fun entry (`coolest-art-01`)

A cyberpunk robot samurai holding a glowing energy katana on a rainy
neon-Tokyo rooftop — with developer in-jokes hidden in the scene
("404: SLEEP NOT FOUND", "DEBUG MODE ON", "git push --force").

## How it works

`main.py` (Python 3 stdlib only) copies the bundled `entry.png` to
`/output/entry.png`, byte-identical. No network, no randomness, no
timestamps — running it twice produces the exact same bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the artwork (1024×1024 JPEG, 329,357 bytes)
- `LICENSE` — MIT

## Run

```sh
python3 main.py   # writes /output/entry.png
```

## License

MIT — see `LICENSE`.
