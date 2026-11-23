"""One Emoji, One Smile — entry program (stdlib only).

Writes exactly one emoji (U+1F970 SMILING FACE WITH HEARTS) as UTF-8 bytes
to $MAKEFUN_OUTPUT_DIR/entry.txt, with no trailing newline and nothing else.
"""

import os
import sys

EMOJI = "\U0001F970"  # U+1F970 SMILING FACE WITH HEARTS
EXPECTED = EMOJI.encode("utf-8")  # b"\xf0\x9f\xa5\xb0" (4 bytes)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Validate: exactly one code point, and it must be an emoji code point.
    if len(EMOJI) != 1:
        print("entry must be exactly one emoji", file=sys.stderr)
        return 1
    cp = ord(EMOJI)
    in_emoji_range = (
        0x1F000 <= cp <= 0x1FAFF  # emoticons, symbols, pictographs, transport
        or 0x2600 <= cp <= 0x27BF  # misc symbols and dingbats
        or 0xFE00 <= cp <= 0xFE0F  # variation selectors (not used here)
        or 0x200D == cp  # ZWJ (not used here)
    )
    if not in_emoji_range:
        print("not an emoji code point", file=sys.stderr)
        return 1

    with open(path, "wb") as f:
        f.write(EXPECTED)

    # Read-back verification: the file on disk must be byte-identical.
    with open(path, "rb") as f:
        back = f.read()
    if back != EXPECTED:
        print("read-back mismatch: %r != %r" % (back, EXPECTED), file=sys.stderr)
        return 1
    if len(back.decode("utf-8")) != 1:
        print("entry is not exactly one character", file=sys.stderr)
        return 1

    print("wrote %d bytes to %s" % (len(EXPECTED), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
