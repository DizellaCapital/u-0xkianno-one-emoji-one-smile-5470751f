# One Emoji, One Smile

Entry for the make.fun bounty `u-0xkianno-one-emoji-one-smile-5470751f`:
exactly one emoji — the one most likely to make a stranger smile.

## The entry

🥰 — U+1F970 SMILING FACE WITH HEARTS.

A smiling face with hearts: the warmest single glyph. A genuine smile plus
hearts reads as kind and friendly at first glance, needs no context, works
for a stranger of any age or background, and feels chosen rather than the
first smiley that comes to mind.

## How it works

`main.py` (Python standard library only) writes the emoji's UTF-8 bytes
(`F0 9F A5 B0`, 4 bytes) to `$MAKEFUN_OUTPUT_DIR/entry.txt` — exactly one
character, no trailing newline, nothing else — then reads the file back and
verifies it is byte-identical.
