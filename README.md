# Static Site Generator

A static site generator written in Python that converts a directory of Markdown files into a full static HTML website — no external dependencies, no JavaScript build tools, just a Python standard library implementation of a Markdown-to-HTML pipeline.

Give it a folder of `.md` files, an HTML template, and a folder of static assets (CSS, images), and it will recursively generate a matching folder of `.html` pages ready to serve or deploy.

## Features

- **Markdown to HTML conversion** — supports headings, paragraphs, blockquotes, ordered/unordered lists, code blocks, bold, italic, inline code, links, and images
- **Recursive page generation** — mirrors your `content/` directory structure into output, converting every `index.md` into an `index.html`
- **Template-based rendering** — inject page title and content into a shared HTML template via `{{ Title }}` and `{{ Content }}` placeholders
- **Static asset copying** — recursively copies everything in `static/` (CSS, images, etc.) into the output directory
- **Configurable base path** — supports deployment under a subpath (e.g. GitHub Pages project sites) by rewriting root-relative `href`/`src` attributes
- **Fully unit tested** — test coverage for the Markdown parsing, HTML node generation, and page generation logic

## Requirements

- Python 3 (no external packages required — standard library only)

## Project structure

```
.
├── content/              # Your site's content, written in Markdown
│   ├── index.md
│   ├── blog/
│   │   └── <post>/index.md
│   └── contact/index.md
├── static/                # Static assets copied as-is (CSS, images, etc.)
│   ├── index.css
│   └── images/
├── template.html          # HTML shell with {{ Title }} / {{ Content }} placeholders
├── docs/                  # Generated site output (safe to delete/regenerate)
├── src/                   # Generator source code
│   ├── main.py            # Entry point
│   ├── copystatic.py      # Recursively copies static/ into docs/
│   ├── generate_content.py# Recursively converts content/ Markdown into docs/ HTML
│   ├── block_markdown.py  # Markdown block-level parsing (headings, lists, quotes, code)
│   ├── inline_markdowns.py# Markdown inline parsing (bold, italic, code, links, images)
│   ├── textnode.py        # TextNode representation of inline text
│   ├── htmlnode.py         # HTML node types used to render final markup
│   └── test_*.py          # Unit tests
├── build.sh               # Builds the site for deployment under /static-site-generator
├── main.sh                # Builds the site and serves it locally on port 8888
└── test.sh                # Runs the unit test suite
```

## Usage

### Build the site

Run the generator directly:

```bash
python3 src/main.py
```

This copies everything from `static/` into `docs/`, then walks `content/`, converting every Markdown file into an HTML page using `template.html`, and writes the result into `docs/`.

By default, all links are generated relative to the root (`/`). To build for deployment under a subpath (e.g. `https://username.github.io/repo-name/`), pass the base path as an argument:

```bash
python3 src/main.py "/repo-name"
```

Or use the provided script, which builds for this project's GitHub Pages path:

```bash
./build.sh
```

### Preview locally

Build the site and start a local HTTP server:

```bash
./main.sh
```

This runs the generator, then serves `docs/`(or `public/`, depending on your build output — see note below) at [http://localhost:8888](http://localhost:8888).

> **Note:** `main.sh` currently `cd`s into a `public` directory before serving, while `main.py` writes output to `docs/`. If you hit a "no such directory" error running `main.sh`, either update the script to `cd docs` or adjust `dir_path_docs` in `main.py` to match your preferred output folder.

### Run tests

```bash
./test.sh
```

or directly with:

```bash
python3 -m unittest discover -s src
```

## How it works

The generation pipeline runs in a few stages:

1. **Static asset copy** (`copystatic.py`) — recursively deletes and rebuilds the output directory, then copies every file from `static/` into it.
2. **Markdown parsing** (`block_markdown.py`, `inline_markdowns.py`, `textnode.py`) — each Markdown file is split into blocks (paragraph, heading, quote, list, code), and each block's inline text is further parsed for bold, italic, inline code, links, and images into a tree of `TextNode` objects.
3. **HTML node tree** (`htmlnode.py`) — `TextNode`s and blocks are converted into `HTMLNode` objects (`LeafNode`/`ParentNode`), which know how to render themselves to an HTML string.
4. **Page generation** (`generate_content.py`) — for every `.md` file in `content/`, the corresponding HTML is generated, the page title (from the first `# heading`) and rendered content are injected into `template.html`, and the result is written to the matching path in the output directory with a `.html` extension.

## Example content

The `content/` directory in this repo includes a sample fan site (a small "Tolkien Fan Club" site with a homepage, a contact page, and a few blog posts) to demonstrate the generator end-to-end. Replace it with your own Markdown content to build your own site.
