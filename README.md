# AI-powered flashcard based PKM tool
A lightweight AI-powered tool that helps users quickly generate entries from uploaded notes, enabling establishing personal PKM, fast retrival, building long-term memory.
The current version focuses on building the retrieval system for personal PKM.
Future development will integrate spaced reprtition (flashcards) to help users build memory.

## Background
As a biochemistry student, my coursemates and I encountered problems of converting learnt concepts into long-term memory and failed to retrive concepts from existing notes. This product aims at helping biological student building memories by solving the failure in quick retrival and 

## Demo and interface preview
The demo is deployed on the streamlit cloud: https://project-001.streamlit.app/

---
### The example text input:

Splicing
pre-mRNA in eukaryotes is spliced to **remove introns** and **ligate exons** together in **nucleus**
- Introns are degraded, Exons exit the nuclear pore
- Donor (at 5' intron = GU) and acceptor (at 3' intron = AG) site (quite random sequence)

![[Pasted image 20260131094906.png]]
snRNA = small nuclear RNA
snRNP = small nuclear ribonucleoproteins = snRNA + protein(s)
- U1 binds 5ʹ donor
- U2 binds bridge --> lariat structure
- U4/U6 re-checks donor
- U5 binds 3ʹ acceptor
![[Pasted image 20260131102617.png]]
Active site is at snRNA not protein
During splicing, intron will be released in **Lariat shape**

Capping, splicing and tailing factors are associated with the CTD of RNAP-II, > whose dynamic phosphorylation pattern ensures the correct timing and order of RNA processing during transcription.
>[!tip] RNA Pol II 的 CTD 充当一个platform，通过不同时间点的不同磷酸化状态，按顺序招募 capping → splicing → polyadenylation / termination 因子。

Post-transcriptional modification is sometimes co-transcriptional

---

The interface was designed by Figma (flashcards interface not done yet):https://www.figma.com/proto/2mES8NsqNM7bEMvbk6Cpb3/Project-001?node-id=0-1&t=uVDlUXMJoPEZMA8E-1
