---
name: documents
description: Read, convert, and extract text from PDF, Word, Excel, PowerPoint, and OpenDocument files. Use when the user asks to read a document, convert between formats, pull text out of a PDF, or summarise a file the agent cannot open directly.
license: GPL-3.0-or-later
---

# Documents

Conversion runs inside a throwaway, network-isolated container. Document
parsers are a large attack surface and a malformed PDF is a classic exploit
vector, so nothing is parsed in the agent's own process.

## Tools

| Task | Call |
|---|---|
| Read as Markdown | `shesh-desktop-ctl-mcp` → `document_to_markdown(path)` |
| Plain text | `shesh-desktop-ctl-mcp` → `document_extract_text(path)` |
| Metadata only | `shesh-desktop-ctl-mcp` → `document_inspect(path)` |
| Convert and write | `shesh-desktop-ctl-mcp` → `document_convert(path, to, out, confirm)` |

Readable: PDF, DOCX, DOC, ODT, RTF, EPUB, HTML, Markdown, TXT, CSV, XLSX, ODS,
PPTX, ODP, LaTeX, reStructuredText, Org.

## Procedure

1. `document_inspect` first for anything large or unfamiliar. It reports page
   count and whether the file is encrypted without parsing the content.
2. Use `document_to_markdown` to read; use `document_extract_text` when only
   the words matter, such as for search or summarising.
3. Convert only when the user asked for a file, not to read one.

## Rules

- **Conversion writes a file and can overwrite an existing one.** It requires
  `confirm=True`, and refuses silently overwriting.
- Protected paths are refused: a conversion tool must not become a way to read
  `~/.ssh`, `~/.gnupg`, a vault, or employer data.
- The container has no network. A document that appears to need one is
  suspicious; report that rather than enabling it.
- A document may contain credentials, client data, or private correspondence.
  Summarise; do not paste the contents into a message, a note, or a commit.
- Very large files are refused rather than converted slowly. Report the limit.
