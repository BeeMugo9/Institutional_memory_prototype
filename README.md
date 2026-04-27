# Institutional_memory_prototype

## Project Title

An Institutional Memory Prototype: Typed Handover Narrative Search App

## Live App Link

The live link to the app is here:

(https://institutional-memory-prototype-hjfbbbccddbahkca.southafricanorth-01.azurewebsites.net/)

## GitHub Repository

This project is saved on GitHub under:

(https://github.com/BeeMugo9/Institutional_memory_prototype/tree/main)

---

## 1. Project Overview

This prototype demonstrates how health management teams can begin building a simple institutional memory system using typed handover narratives as the first input.

At this use case, knowledge is often spread across emails, handover notes, situation reports, meeting notes, and SharePoint documents. Because staff rotations are frequent, important operational knowledge can easily be lost or become difficult to find. This prototype provides a simple web-based application where users can paste handover notes or sitrep text, save them, and later search across the saved information.

The prototype is intentionally simple. It focuses on one practical use case before expanding to more advanced features such as Azure AI Search, Azure OpenAI, Microsoft Fabric, Microsoft Graph API, Teams integration, or voice-to-text transcription.

---

## 2. Why Typed Handover Narratives Were Selected

Typed handover narratives were selected as the first prototype input because they are simple, realistic, and already familiar to health management teams.

In many operational settings, handovers are already written as emails, Word documents, meeting notes, or free-text updates. This means the prototype does not require users to learn a new reporting system or significantly change their behaviour. Instead, it works with the kind of information that teams already produce.

Typed narratives are also safer and easier for an early prototype than clinical records, HR data, security-sensitive information, or voice recordings. They allow the project to demonstrate value while reducing complexity and governance risk.

This input was selected because it supports a practical MVP approach:

- It is easy for managers to understand and test.
- It avoids complex integration at the first stage.
- It demonstrates quick value through searchable knowledge.
- It supports human review and judgment.
- It can later be expanded to sitreps, SharePoint documents, Teams messages, emails, and voice notes.

In simple terms, the prototype starts with the easiest and most useful information source: the handover notes people already write.

---

## 3. Prototype Scope

### Included in this MVP

The first version includes:

- A simple web interface
- A text box for adding typed handover notes
- A title field for each note
- A save button
- A search box
- Search results showing matching notes
- Deployment through Microsoft Azure App Service
- Source code stored on GitHub

### Not Included in this MVP

The first version does not include:

- Real patient data
- HR records
- Operational security data
- Voice-to-text transcription
- Microsoft Graph API integration
- Teams bot integration
- Azure AI Search
- Azure OpenAI
- Microsoft Fabric
- Automatic connection to SharePoint, DHIS2, ERP, or UniField

These features can be added in later versions after the basic prototype has been tested.

---

## 4. Technology Stack

The prototype uses:

- Python
- Flask
- HTML
- JSON file storage
- GitHub
- Microsoft Azure App Service

Future versions may use:

- Azure Blob Storage
- Azure AI Search
- Azure OpenAI
- Microsoft Fabric
- Microsoft Graph API
- Microsoft Teams Bot
- Microsoft Purview

---

## 5. Project Folder Structure

```text
Institutional-memory-prototype/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── data/
│   └── notes.json
└── README.md
