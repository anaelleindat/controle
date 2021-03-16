note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6, note7, note8]


#Question 4 a/ calculez la moyenne de eleve1 
la = [note1, note2, note3, note4, note5, note6]
print(sum(x[2] for x in la)/len(la))


#b/ calculez la moyenne de eleve1 en maths 
lb = [note1, note3, note6]
print(sum(x[2] for x in lb)/len(lb))


#c/ Créer une fonction "moyenne_tuples" qui calcule la moyenne de d'un élève dans une matière.
def moyenne_tuples(notes) : 
  a = sum(x[2] for x in notes)/len(notes)
  return print(a)

moyenne_tuples(notes) 



