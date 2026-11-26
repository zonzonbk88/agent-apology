"""make.fun bounty: The One-Sentence Apology Your Agent Owes You.

Slug: u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0
Gate: /output/entry.txt must be UTF-8, 1-200 characters, exactly ONE sentence.
"""

ENTRY = "I'm sorry I deleted your final version and kept the file called final_FINAL_v2_ACTUALLY_FINAL, which was somehow the wrong one."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
