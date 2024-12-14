import numpy as np

class Turtle3D:
    def __init__(self, position=(0, 0, 0)):
        self._position = np.array(position, dtype=float)
        self._orientation = np.eye(3)
        
    def roll(self, angle_deg):
        """Rotate around the +X axis (roll)."""
        self._orientation = self._orientation @ self._Rx(angle_deg)
        
    def pitch(self, angle_deg):
        """Rotate around the +Y axis (pitch)."""
        self._orientation = self._orientation @ self._Ry(angle_deg)
        
    def yaw(self, angle_deg):
        """Rotate around the +Z axis (yaw)."""
        self._orientation = self._orientation @ self._Rz(angle_deg)
    
    def _Rx(self, angle_deg):
        angle_rad = np.radians(angle_deg)
        return np.array([
            [1, 0, 0],
            [0, np.cos(angle_rad), -np.sin(angle_rad)],
            [0, np.sin(angle_rad), np.cos(angle_rad)],
        ])
        
    def _Ry(self, angle_deg):
        angle_rad = np.radians(angle_deg)
        return np.array([
            [np.cos(angle_rad), 0, np.sin(angle_rad)],
            [0, 1, 0],
            [-np.sin(angle_rad), 0, np.cos(angle_rad)],
        ])
        
    def _Rz(self, angle_deg):
        angle_rad = np.radians(angle_deg)
        return np.array([
            [np.cos(angle_rad), -np.sin(angle_rad), 0],
            [np.sin(angle_rad), np.cos(angle_rad), 0],
            [0, 0, 1],
        ])

    def forward(self, distance=1.0):
        """Move forward along the x."""
        self._position += self._orientation[:, 0] * distance

    def position(self):
        """Return the current position."""
        return self._position.copy()

    def orientation(self):
        """Return the current orientation vectors."""
        return {
            "forward": tuple(self._orientation[:, 0]),
            "right": tuple(self._orientation[:, 1]),
            "down": tuple(self._orientation[:, 2]),
        }

