# Susu Group Manager

A small Python program that keeps the records for a **susu** (rotating savings group): every member pays the same amount each week, and one member collects the whole pot in turn.

## What it does

- Works out the size of the weekly pot
- Shows whose turn it is to collect, for any week, going round in a circle
- Keeps a ledger of who has paid for which week, refusing unknown names and double payments
- Lists who hasn't paid and how much each member owes
- Prints a weekly report ready to paste into WhatsApp
- Reads amounts typed in different ways (`50`, `GH₵50`, `ghs 1,000.00`) and rejects nonsense safely

## Run it

```bash
python3 susu.py
```

Edit `MEMBERS` and `CONTRIBUTION` at the top to match your own group.

## What I learnt

Lists, dictionaries, loops, functions that return values, f-strings, the `%` operator for going round in a circle, and `try`/`except` for messy input.

Built as a project in the Codestride Python Beginner course.
