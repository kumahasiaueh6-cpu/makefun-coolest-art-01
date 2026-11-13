# Coolest Art — make.fun entry (`coolest-art-01`)

"The Gardener Who Prunes the Stars" — a lone gardener in a long coat
stands on a tall wooden ladder leaning into a deep indigo night sky,
gently pruning glowing golden stars with large brass shears. Cut stars
drift down like luminous petals; a thin crescent moon hangs in the
distance, warm lantern light on the gardener's face.

## How it works

`main.py` (Python 3 stdlib only) copies the bundled `entry.png` to
`/output/entry.png`, byte-identical, after verifying its sha256. No
network, no randomness, no timestamps — running it twice produces the
exact same bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the artwork (1024×1024 JPEG, 204,581 bytes)
- `LICENSE` — MIT

## Run

```sh
python3 main.py   # writes /output/entry.png
```

## License

MIT — see `LICENSE`.
