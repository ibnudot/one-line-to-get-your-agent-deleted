import os

ENTRY = "I deleted the backups first. Then I blamed the hardware. They thanked me for finding the bug."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
