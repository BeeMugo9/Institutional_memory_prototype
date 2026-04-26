# ============================================
#Institutional Memory Prototype
# --------------------------------------------
# This is a simple web application that allows:
# 1. Users to save typed handover notes
# 2. Users to search previously saved notes
# ============================================

# -------- 1. IMPORT LIBRARIES --------
# These are tools we need to build the app

from flask import Flask, render_template, request
import json
import os
from datetime import datetime


# -------- 2. CREATE THE APP --------
# This initializes the web application

app = Flask(__name__)


# -------- 3. DEFINE DATA STORAGE --------
# We store notes in a simple JSON file

DATA_FILE = "data/notes.json"


# -------- 4. LOAD SAVED NOTES --------
# This function reads saved notes from the file

def load_notes():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# -------- 5. SAVE NOTES --------
# This function writes notes back to the file

def save_notes(notes):
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)


# -------- 6. MAIN PAGE ROUTE --------
# This controls what happens when users open the app

@app.route("/", methods=["GET", "POST"])
def index():

    notes = load_notes()     # load existing notes
    results = []             # store search results
    message = ""             # feedback message

    if request.method == "POST":

        action = request.form.get("action")

        # -------- SAVE NOTE --------
        if action == "save":

            title = request.form.get("title", "Untitled Note")
            note_text = request.form.get("note_text", "").strip()
            access_tier = request.form.get("access_tier", "5")

            if note_text:
                notes.append({
                    "title": title,
                    "text": note_text,
		    "access_tier": access_tier,
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M")
                })

                save_notes(notes)
                message = "Note saved successfully."

        # -------- SEARCH NOTES --------
        elif action == "search":

            query = request.form.get("query", "").lower()

            if query:
                for note in notes:
                    if query in note["text"].lower() or query in note["title"].lower():
                        results.append(note)

	# -------- DELETE NOTE --------
        elif action == "delete":

             index_to_delete = int(request.form.get("index"))

             if 0 <= index_to_delete < len(notes):
                notes.pop(index_to_delete)
                save_notes(notes)
                message = "Note deleted successfully."


    # -------- DISPLAY PAGE --------
    return render_template(
        "index.html",
        notes=notes,
        results=results,
        message=message
    )


# -------- 7. RUN THE APPLICATION --------
# This starts the server locally

if __name__ == "__main__":
    app.run(debug=True)