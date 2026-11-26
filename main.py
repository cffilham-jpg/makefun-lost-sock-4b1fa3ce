"""Write one lost sock status update to the configured output directory.
The duvet-cover rescue request ends with a smaller, sock-sized surprise.
"""

import os
from pathlib import Path


LINE = "Day 12 inside the duvet cover. Send a smaller sock."

if not LINE.strip():
    raise ValueError("The entry line must not be empty or whitespace-only.")
if len(LINE) > 120:
    raise ValueError("The entry line must be at most 120 characters.")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
