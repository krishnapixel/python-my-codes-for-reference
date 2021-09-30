from docplex.mp.model import Model
m = model(name = 'Telephone Production')
desk = m.continuous_var(name = 'desk')
cell = m.continuous_var(name = 'cell')
m.add_constraint(desk>=100)
m.add_constraint(cell>=100)
