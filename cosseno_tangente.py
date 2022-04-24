#Author: Elaine Dias Pires

import math

angle = float(input('Type an angle:'))
sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))

print('The angle {} has sine of {:.2f}, cosine of {:.2f} and tangent of {:.2f} ' 
.format(angle, sine, cosine, tangent))

