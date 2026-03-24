#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PACKS_DIR = ROOT / "packs"


def load_pack(name: str) -> dict:
    path = PACKS_DIR / f"{name}.json"
    if not path.exists():
        available = ", ".join(sorted(p.stem for p in PACKS_DIR.glob("*.json")))
        raise SystemExit(f"Unknown pack: {name}\nAvailable packs: {available}")
    return json.loads(path.read_text(encoding="utf-8"))


def read_source_content(path_str: str) -> str:
    """Read a source file, extracting markdown from .ipynb if needed."""
    path = Path(path_str)
    if not path.exists():
        raise SystemExit(f"Source file not found: {path_str}")
    if path.suffix == ".ipynb":
        nb = json.loads(path.read_text(encoding="utf-8"))
        parts = []
        for cell in nb.get("cells", []):
            if cell.get("cell_type") == "markdown":
                parts.append("".join(cell.get("source", [])))
            elif cell.get("cell_type") == "code":
                code = "".join(cell.get("source", []))
                if code.strip():
                    parts.append(f"```python\n{code}\n```")
        return "\n\n".join(parts)
    return path.read_text(encoding="utf-8")


def render_runtime_block(
    goal: str,
    level: str,
    session_length: str,
    sources: list[str],
    embed: bool = False,
) -> str:
    lines = [
        "## Runtime Context",
        f"- Goal: {goal or 'Not specified'}",
        f"- Learner level: {level or 'Not specified'}",
        f"- Session length: {session_length or 'Not specified'}",
    ]
    if sources:
        lines.append("- Source files:")
        lines.extend(f"  - {source}" for source in sources)
    else:
        lines.append("- Source files: None provided")

    if embed and sources:
        lines.append("")
        lines.append("## Source Content")
        for source in sources:
            lines.append(f"\n### {Path(source).name}\n")
            lines.append(read_source_content(source))

    return "\n".join(lines)


def build_prompt(
    pack_name: str,
    goal: str,
    level: str,
    session_length: str,
    sources: list[str],
    embed: bool = False,
) -> str:
    pack = load_pack(pack_name)
    sections = [f"# Pack: {pack['name']}", "", pack.get("description", ""), ""]
    for rel_module in pack["modules"]:
        module_path = ROOT / rel_module
        if not module_path.exists():
            raise SystemExit(f"Missing module: {rel_module}")
        title = f"## Module: {rel_module}"
        body = module_path.read_text(encoding="utf-8").strip()
        sections.extend([title, "", body, ""])
    sections.append(render_runtime_block(goal, level, session_length, sources, embed=embed))
    sections.append("")
    sections.append(
        "## Final Instruction\n"
        "위 모듈 규칙을 모두 적용해 응답하라. 자료를 이미 읽었다고 가정하지 말고, "
        "한국어 사용자에게 실제로 가르치는 방식으로 진행하라."
    )
    return "\n".join(sections).strip() + "\n"


def cmd_list(_: argparse.Namespace) -> int:
    for pack_path in sorted(PACKS_DIR.glob("*.json")):
        pack = json.loads(pack_path.read_text(encoding="utf-8"))
        print(f"{pack['name']}: {pack.get('description', '')}")
    return 0


def cmd_build(args: argparse.Namespace) -> int:
    prompt = build_prompt(
        pack_name=args.pack,
        goal=args.goal,
        level=args.level,
        session_length=args.session_length,
        sources=args.source,
        embed=args.embed,
    )
    if args.output:
        output_path = Path(args.output)
        if not output_path.is_absolute():
            output_path = ROOT / output_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(prompt, encoding="utf-8")
    else:
        sys.stdout.write(prompt)
    return 0


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Assemble Korean study/humanize prompt packs.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List available packs")
    list_parser.set_defaults(func=cmd_list)

    build_parser = subparsers.add_parser("build", help="Build a prompt from a pack")
    build_parser.add_argument("pack", help="Pack name without .json")
    build_parser.add_argument("--goal", default="", help="Learning or rewriting goal")
    build_parser.add_argument("--level", default="", help="Learner level")
    build_parser.add_argument("--session-length", default="", help="Session duration")
    build_parser.add_argument("--source", action="append", default=[], help="Source file path (.md or .ipynb)")
    build_parser.add_argument("--embed", action="store_true", help="Embed source file contents into the prompt")
    build_parser.add_argument("--output", help="Output file path")
    build_parser.set_defaults(func=cmd_build)

    return parser


def main() -> int:
    parser = make_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
