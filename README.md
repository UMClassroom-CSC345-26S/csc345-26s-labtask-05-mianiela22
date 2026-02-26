[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/z-U2J4e_)
# Two Ends of Knowledge

This labtask has two parts. The first is at the "low end" of Knowledge Representation -
checking for logical consequence in propositional logic. The second is at the high end" -
displaying ontological knowledge in a knowledge graph.

1. Logical Consequence in Propositional Logic
   - Use a truth table to decide whether or not `p | q` is a logical consequence of the axioms
     ```
     p | q | r
     r => (p | q)
     (q & r) => p
     ~p | q | r
     ```
     Put your answer and the truth table (I suggest using a spreadsheet to do it neatly) in a PDF file called `LC1.pdf`.
   - Use a truth table to decide whether or not `q & (r => p)` is a logical consequence of the axioms
     ```
     p => (q | r)
     p | q | r
     ~q => (p | ~r)
     (q & r) => p
     ```
     Put your answer and the truth table (I suggest using a spreadsheet to do it neatly) in a PDF file called `LC2.pdf`.

3. Ontological Knowledge Graph  
   On 20th January 2026 the Miami Hurricanes lost the College Football Playoff National 
   Championship to the Indiana Hoosiers, 27-21. Carson Beck was a member of the Miami team.
   Represent this using the terms:
   - `CFPNC_2026`
   - `Miami_Hurricanes`
   - `Indiana_Hoosiers`
   - `20_January_2026`
   - `27`
   - `21`
   - `Carson_Beck`

   connected to terms from the SUMO ontology.
   For example, `CFPNC_2026` is an `instance` of the SUMO term `FootballUS`, which is a `subclass`
   of `TeamSport`, which is a subclass of `Sport`, etc., which is a subclass of `Physical` 
   which is a subclass `Entity` (you must fill in "etc.").
   The knowledge you must capture is:
   - `Miami_Hurricanes` lost `CFPNC_2026`
   - `Indiana_Hoosiers` won `CFPNC_2026`
   - `20_January_2026` is_date `CFPNC_2026`
   - `27` winning_score `CFPNC_2026`
   - `21` losing_score `CFPNC_2026`
   - `Carson_Beck` contestParticipant `CFPNC_2026`
   - `Carson_Beck` member `Miami_Hurricanes`
   
   The SUMO starting points you must use are:
   - `FootballUS` (for `CFPNC_2026`)
   - `SportsTeam` (for `Miami_Hurricanes` and `Indiana_Hoosiers`)
   - `Day` (for `20_January_2026`)
   - `NonnegativeInteger` (for `27` and `21`)
   - `Man` (for `Carson_Beck`)
     
   All the SUMO subclass hierarchies must end at `Entity`.
   
   Write out all your Thing-Relationship-Thing tripes in a text file `Football.txt`.
   Render the knowledge in a knowledge graph, and save it in a file `Football.png` (take a
   screenshot).
   Submit `Football.txt`, and `Football.png`.
