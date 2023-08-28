# door-deck
 
Generates door decks provided a folder of photos and a CSV containing a list of names and room numbers.

## Installation
1. Download repository. 
2. Install **Pillow**, **Pandas**, and **NumPy**.

```
python pip install -r pkg.txt
```

## Usage
1. Place photos you want on your door deck inside `photos/`. Make sure the photos are in **PNG** format.
- Do **not** delete `tag.jpg`.
2. Populate `tags.csv` with your list of names. An example is included.
- FORMAT: `FirstName LastName, FirstName, Room`
3. Execute `deck.py`

```
python deck.py
```

Blank door decks are found in `tags/` and named decks are found in `photos/`. `deck_all.pdf` collects all the named and blank decks in one easy file for printing. Print multiple decks on 1 page to save on paper and ink.
