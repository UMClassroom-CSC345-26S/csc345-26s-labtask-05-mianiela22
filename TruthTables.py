import itertools
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

#-THE FUNCTIONS
def truth_val(b):
    " making it T or F"
    return "T" if b else "F"



#LC1 example
def make_lc1():

#pdf
    doc = SimpleDocTemplate("LC1.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('CustomTitle', parent=styles['Title'], fontSize=14, spaceAfter=12)
    story.append(Paragraph("LC1: Is  p | q  a logical consequence of the axioms?", title_style))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Axioms:</b>", styles['Normal']))
    story.append(Paragraph("A1:  p | q | r", styles['Normal']))
    story.append(Paragraph("A2:  r =&gt; (p | q)", styles['Normal']))
    story.append(Paragraph("A3:  (q &amp; r) =&gt; p", styles['Normal']))
    story.append(Paragraph("A4:  ~p | q | r", styles['Normal']))
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Conclusion:</b>  C:  p | q", styles['Normal']))
    story.append(Spacer(1, 12))


#table head
    header = ["p", "q", "r", "A1\np|q|r", "A2\nr=>(p|q)", "A3\n(q&r)=>p", "A4\n~p|q|r",
              "All Axioms\nTRUE?", "C\np|q", "LC\nholds?"]
    rows = [header]

#generating t/f
    for p_val, q_val, r_val in itertools.product([True, False], repeat=3):
        p, q, r = p_val, q_val, r_val

#translating operators
        a1 = p or q or r                       # p | q | r
        a2 = (not r) or (p or q)               # r => (p | q)
        a3 = (not (q and r)) or p              # (q & r) => p  
        a4 = (not p) or q or r                 # ~p | q | r


        all_axioms = a1 and a2 and a3 and a4
        conclusion = p or q                    # p | q


        if all_axioms:
            lc_check = "YES" if conclusion else "NO*"
        else:
            lc_check = "-"

#adding rows
        row = [truth_val(p), truth_val(q), truth_val(r),
               truth_val(a1), truth_val(a2), truth_val(a3), truth_val(a4),
               "YES" if all_axioms else "NO",
               truth_val(conclusion), lc_check]
        rows.append(row)

#----Format the table for the PDF
    col_widths = [0.4*inch, 0.4*inch, 0.4*inch, 0.65*inch, 0.75*inch, 0.75*inch, 0.65*inch,
                  0.8*inch, 0.5*inch, 0.55*inch]
    table = Table(rows, colWidths=col_widths)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4472C4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTSIZE', (0, 0), (-1, 0), 7),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#D9E2F3')]),
    ])

#highlight if all true
    for i in range(1, len(rows)):
        if rows[i][7] == "YES":
            style.add('BACKGROUND', (7, i), (7, i), colors.HexColor('#C6EFCE'))
            style.add('BACKGROUND', (8, i), (8, i), colors.HexColor('#C6EFCE'))

    table.setStyle(style)
    story.append(table)
    story.append(Spacer(1, 16))

#-conclusion
    story.append(Paragraph("<b>Analysis:</b>", styles['Normal']))
    story.append(Spacer(1, 6))

    model_rows = []
    for i in range(1, len(rows)):
        if rows[i][7] == "YES":
            model_rows.append(i)

    story.append(Paragraph(
        f"There are {len(model_rows)} interpretation(s) where all axioms are TRUE (models).",
        styles['Normal']))
    story.append(Spacer(1, 6))

#check if true in all models
    all_conclusions_true = all(rows[i][8] == "T" for i in model_rows)

    if all_conclusions_true:
        story.append(Paragraph(
            "In every model (row where all axioms are TRUE), the conclusion  p | q  is also TRUE.",
            styles['Normal']))
        story.append(Spacer(1, 6))
        story.append(Paragraph(
            "<b>Conclusion: YES, p | q IS a logical consequence of the axioms.</b>",
            styles['Normal']))
    else:
        story.append(Paragraph(
            "There exists at least one model where the conclusion  p | q  is FALSE.",
            styles['Normal']))
        story.append(Spacer(1, 6))
        story.append(Paragraph(
            "<b>Conclusion: NO, p | q is NOT a logical consequence of the axioms.</b>",
            styles['Normal']))

#----Build the PDF
    doc.build(story)
    print("Saved: LC1.pdf")


#--------------------------------------------------------------------------------------------------
def make_lc2():

#pdf
    doc = SimpleDocTemplate("LC2.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('CustomTitle', parent=styles['Title'], fontSize=14, spaceAfter=12)
    story.append(Paragraph("LC2: Is  q &amp; (r =&gt; p)  a logical consequence of the axioms?", title_style))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Axioms:</b>", styles['Normal']))
    story.append(Paragraph("A1:  p =&gt; (q | r)", styles['Normal']))
    story.append(Paragraph("A2:  p | q | r", styles['Normal']))
    story.append(Paragraph("A3:  ~q =&gt; (p | ~r)", styles['Normal']))
    story.append(Paragraph("A4:  (q &amp; r) =&gt; p", styles['Normal']))
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Conclusion:</b>  C:  q &amp; (r =&gt; p)", styles['Normal']))
    story.append(Spacer(1, 12))


    header = ["p", "q", "r", "A1\np=>(q|r)", "A2\np|q|r", "A3\n~q=>(p|~r)", "A4\n(q&r)=>p",
              "All Axioms\nTRUE?", "C\nq&(r=>p)", "LC\nholds?"]
    rows = [header]

#making the t/f
    for p_val, q_val, r_val in itertools.product([True, False], repeat=3):
        p, q, r = p_val, q_val, r_val

#translating again 
        a1 = (not p) or (q or r)               # p => (q | r)  ... ~p | (q | r)
        a2 = p or q or r                       # p | q | r
        a3 = q or (p or (not r))               # ~q => (p | ~r) ... q | p | ~r
        a4 = (not (q and r)) or p              # (q & r) => p  ... ~(q & r) | p

#check for all true
        all_axioms = a1 and a2 and a3 and a4
        r_implies_p = (not r) or p             # r => p  ... ~r | p
        conclusion = q and r_implies_p         # q & (r => p)

#does it hold
        if all_axioms:
            lc_check = "YES" if conclusion else "NO*"
        else:
            lc_check = "-"


        row = [truth_val(p), truth_val(q), truth_val(r),
               truth_val(a1), truth_val(a2), truth_val(a3), truth_val(a4),
               "YES" if all_axioms else "NO",
               truth_val(conclusion), lc_check]
        rows.append(row)

#table pdf
    col_widths = [0.4*inch, 0.4*inch, 0.4*inch, 0.7*inch, 0.6*inch, 0.8*inch, 0.75*inch,
                  0.8*inch, 0.65*inch, 0.55*inch]
    table = Table(rows, colWidths=col_widths)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4472C4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTSIZE', (0, 0), (-1, 0), 7),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#D9E2F3')]),
    ])

#highlights
    for i in range(1, len(rows)):
        if rows[i][7] == "YES":
            style.add('BACKGROUND', (7, i), (7, i), colors.HexColor('#C6EFCE'))
            style.add('BACKGROUND', (8, i), (8, i), colors.HexColor('#C6EFCE'))
            if rows[i][9] == "NO*":
                style.add('BACKGROUND', (8, i), (8, i), colors.HexColor('#FFC7CE'))
                style.add('BACKGROUND', (9, i), (9, i), colors.HexColor('#FFC7CE'))

    table.setStyle(style)
    story.append(table)
    story.append(Spacer(1, 16))


    story.append(Paragraph("<b>Analysis:</b>", styles['Normal']))
    story.append(Spacer(1, 6))


    model_rows = []
    counterexample_rows = []
    for i in range(1, len(rows)):
        if rows[i][7] == "YES":
            model_rows.append(i)
            if rows[i][8] == "F":
                counterexample_rows.append(i)

    story.append(Paragraph(
        f"There are {len(model_rows)} interpretation(s) where all axioms are TRUE (models).",
        styles['Normal']))
    story.append(Spacer(1, 6))

    if len(counterexample_rows) == 0:
        story.append(Paragraph(
            "In every model, the conclusion  q &amp; (r =&gt; p)  is also TRUE.",
            styles['Normal']))
        story.append(Spacer(1, 6))
        story.append(Paragraph(
            "<b>Conclusion: YES, q &amp; (r =&gt; p) IS a logical consequence of the axioms.</b>",
            styles['Normal']))
    else:
        story.append(Paragraph(
            f"There are {len(counterexample_rows)} counterexample(s) where all axioms are TRUE "
            "but the conclusion is FALSE (marked NO* in the table).",
            styles['Normal']))
        story.append(Spacer(1, 6))
        for ci in counterexample_rows:
            pv, qv, rv = rows[ci][0], rows[ci][1], rows[ci][2]
            story.append(Paragraph(
                f"  Counterexample: p={pv}, q={qv}, r={rv}", styles['Normal']))
        story.append(Spacer(1, 6))
        story.append(Paragraph(
            "<b>Conclusion: NO, q &amp; (r =&gt; p) is NOT a logical consequence of the axioms.</b>",
            styles['Normal']))

#pdf
    doc.build(story)
    print("Saved: LC2.pdf")


#--------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    make_lc1()
    make_lc2()
