import numpy as np
import math
import random

class Ball:
    def __init__(self, x, y, initVector) -> None:
        """初始化球

        Args:
            x (float): X座標
            y (float): Y座標
            initVector (tuple): 初始向量(單位向量)
        """
        self.locX = x
        self.locY = y
        self.vector = initVector
        self.speed = 0.15
        self.color = (255, 255, 255)
    
    def rotate(self, angle):
        angle_rad = math.radians(angle)
        rotate_matrix = np.array([[math.cos(angle_rad), -math.sin(angle_rad)], [math.sin(angle_rad), math.cos(angle_rad)]])
        result = np.dot(rotate_matrix, self.vector)
        self.vector = (float(result[0]), float(result[1]))
    
    def reflect_vector(self, v, n):
        # 確保法向量為單位向量
        n = n / np.linalg.norm(n)
        # 計算反射後的速度
        v_reflected = v - 2 * np.dot(v, n) * n
        return (float(v_reflected[0]), float(v_reflected[1]))
    
    def bounce(self, normal):
        """碰牆時的反射

        Args:
            normal (tuple): 法向量
        """
        self.vector = self.reflect_vector(self.vector, normal)
        random_angle = random.randint(-5, 5)
        self.rotate(random_angle)
        self.move()
    
    def move(self):
        if self.vector[0] > 0.9 or self.vector[0] < -0.9 or self.vector[1] > 0.9 or self.vector[1] < -0.9:
            self.vector = (0, -1)
            random_angle = random.randint(30, 60)
            self.rotate(random_angle)
            
        self.locX += self.vector[0] * self.speed
        self.locY += self.vector[1] * self.speed