import numpy as np
class Ball:
    def __init__(self, x, y, initSpeedVector) -> None:
        self.locX = x
        self.locY = y
        self.speedVector = initSpeedVector
        self.color = (255, 255, 255)
    
    def reflect_vector(self, v, n):
        # 確保法向量為單位向量
        n = n / np.linalg.norm(n)
        # 計算反射後的速度
        v_reflected = v - 2 * np.dot(v, n) * n
        return (int(v_reflected[0]), int(v_reflected[1]))

    def bounce(self, normal):
        """碰牆時的反射

        Args:
            normal (tuple): 法向量
        """
        self.speedVector = self.reflect_vector(self.speedVector, normal)
    
    def move(self):
        self.locX += self.speedVector[0] * 0.1
        self.locY += self.speedVector[1] * 0.1