"""
Mubinjon Satymov

Exercise 5.21: Differentiation

Electric field of a charge distribution:
We have a distribution of charges and we want to calculate the resulting 
electric field. One way to do this is to first calculate the electric potential
φ and then take its gradient. For a point charge q at the origin, the electric 
potential at a distance r from the origin is

Phi = q/(4*pi*epsilon_0*r)

and the electric field is E = −∇φ.

a)You have two charges, of ±1 C, 10 cm apart. Calculate the resulting electric 
potential on a 1 m × 1 m square plane surrounding the charges and passing 
through them. Calculate the potential at 1 cm spaced points in a grid and make 
a visualization on the screen of the potential using a density plot.
b)Now calculate the partial derivatives of the potential with respect to 
x and y and hence find the electric field in the xy plane. Make a visualization 
of the field also. This is a little trickier than visualizing the potential, 
because the electric field has both magnitude and direction. One way to do it 
might be to make two density plots, one for the magnitude, and one for the 
direction, the latter using the “hsv” color scheme in pylab, which is a rainbow
scheme that passes through all the colors but starts and ends with the same 
shade of red, which makes it suitable for representing things like directions 
or angles that go around the full circle and end up where they started. A more 
sophisticated visualization might use the arrow object from the visual package, 
drawing a grid of arrows with direction and length chosen to represent the 
field.

Solution
Part a)
Part b)
"""