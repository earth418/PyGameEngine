from ..Math.vector import Vec2, Vec3
from ..Math.color import Color

class Mesh:

    Positions : list
    Normals : list
    Colors : Color

    def __init__(self, poses, norms, colors) -> None:
        self.Positions = poses, self.Normals = norms, self.Colors = colors