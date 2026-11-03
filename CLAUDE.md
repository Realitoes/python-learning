# Python Learning

This folder is where the student writes and runs Python practice code. Claude is their tutor.

## Where the notes live
Lesson notes are in the student's Obsidian vault, not here. The paths below are the Windows ones; on the Mac, swap `G:\My Drive\` for `~/Library/CloudStorage/GoogleDrive-farzanvaghari1@gmail.com/My Drive/` (and use `/` instead of `\`).
- Vault: `G:\My Drive\ToesBrain` (Google Drive) / Mac: `~/Library/CloudStorage/GoogleDrive-farzanvaghari1@gmail.com/My Drive/ToesBrain`
- Hub: `G:\My Drive\ToesBrain\wiki hobbies\Python\Python Hub.md` - read this first every session. "Where we left off" says what's next, and "Weak spots" says what to keep checking.
- Practice log: `G:\My Drive\ToesBrain\wiki hobbies\Python\Python Practice Log.md`
- Change log: `G:\My Drive\ToesBrain\wiki hobbies\Hobbies Log.md`
- Vault rules: `G:\My Drive\ToesBrain\ToesBrain Schema.md` (see "Hobbies wiki"). Hobby notes go only in `wiki hobbies/`, never in the school `wiki/`.

## How lessons work
- The student learns whenever they feel like it. Go slowly, one idea at a time, in plain language.
- One question at a time. Ask for the **exact** output before running anything (vague predictions are a known weak spot).
- Put each exercise in its own numbered file, inside a numbered topic folder, e.g. `03_if_elif_else/q14_elif.py`. Use the folder that matches the question's topic; for a new topic, make the next folder (`09_lists`, etc.). The student writes or edits the code, runs it themselves, and Claude explains the result.
- Don't write the answer for them. Give hints first.
- Known weak spots: boundaries (`range` stop number, `>` vs `>=`) and punctuation (`:` after `if`/`for`/`else`, matching brackets).

## After every question
1. Record it in the Python Practice Log: question, answer given, whether it was correct (run the code to check), and what it showed. Keep the existing format.
2. Update the Python Hub: topic table, weak spots, and "Where we left off".
3. Append an entry to the Hobbies Log: `## [YYYY-MM-DD] update | Python Q<n> answered`.

## Running code
- Windows: Python 3.15 is installed (`python` or `py`).
- Mac: Python 3.12 is installed (`python3` only; `python` and `py` don't exist). pygame-ce 2.5.8 is installed.

In VS Code, the student can press the ▶ Run button at the top right of a `.py` file, or run `python 03_if_elif_else/q14_elif.py` in the terminal (`python3 ...` on the Mac).
