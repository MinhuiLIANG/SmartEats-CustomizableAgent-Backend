## Backend of SmartEats based on agent customization [cui-25-full paper]
This repo includes the backend for a dietary recommender system that features a customizable conversational agent, as well as a non-customizable baseline. The customization interface looks like this (see the figure below):


**🍱 The entrance of this project is `/Central/apifile.py` (for customizable version) and `/Central/apifilebl.py` (for baseline).**

**🍝 The project structure is described as follows:**
- `Central`: apis connecting to the frontend;
- `Controllers`: integrating components to form functions;
- `Components`: LLM units;
- `DAO`: crud functions connecting to the database;
- `fixedSentences.py`: pre-defined sentences;
- `topicTree.py`: a tree structure for interaction flow control.

**🥠 What you need to configure:**
- OpenAI api-key;
- Firebase credentials under `/DAO`;
- Database urls in `/DAO/dbops.py`.
- Switching customizable v.s. baseline version in `/DAO/dbops.py`, line 19.
- Pre-defining the characteristics or the conversational agent of baseline in `/DAO/dbops.py`, line 108 & 109.
