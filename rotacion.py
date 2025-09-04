import numpy as np


def rot_x(x: float, y: float, z: float, theta: float) -> np.ndarray:
    '''
    Descripcion: Rotar un punto en el espacio tridimensional alrededor del eje X por un ángulo dado.

    Parameters:
        x (float): Coordenada X del punto original.
        y (float): Coordenada Y del punto original.
        z (float): Coordenada Z del punto original.
        theta (float): Ángulo de rotación en radianes.

    Returns:
        np.ndarray: Vector rotado como un arreglo de NumPy [x', y', z'].
    '''
    p = np.array([x, y, z])
    R = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
        ])
    return R @ p

def rot_y(x: float, y: float, z: float, theta:float)-> np.ndarray:
    '''
    Descripcion: Rota un punto en el espacio tridimensional alrededor del eje Y por un ángulo dado.

    Parameters:
        x (float): Coordenada X del punto original.
        y (float): Coordenada Y del punto original.
        z (float): Coordenada Z del punto original.
        theta (float): Ángulo de rotación en radianes.

    Returns:
        np.ndarray: Vector rotado como un arreglo de NumPy [x', y', z'].
    '''
    p = np.array([x, y, z])
    R = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
        ])
    return R @ p

def rot_z(x: float, y: float, z: float, theta: float) -> np.ndarray:
    '''
    Descripcion: Rota un punto en el espacio tridimensional alrededor del eje Z por un ángulo dado.

    Parameters:
        x (float): Coordenada X del punto original.
        y (float): Coordenada Y del punto original.
        z (float): Coordenada Z del punto original.
        theta (float): Ángulo de rotación en radianes.

    Returns:
        np.ndarray: Vector rotado como un arreglo de NumPy [x', y', z'].
    '''
    p = np.array([x, y, z])
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
        ])
    return R @ p


def rotar(x: float, y: float, z: float, theta: float, axis: str) -> np.ndarray:
    '''
    Descripcion: Rota un punto en el espacio tridimensional alrededor de un eje especificado.

    Parameters:
        x (float): Coordenada X del punto original.
        y (float): Coordenada Y del punto original.
        z (float): Coordenada Z del punto original.
        theta (float): Ángulo de rotación en radianes.
        axis (str): Eje de rotación ('x', 'y', 'z').

    Returns:
        np.ndarray: Vector rotado como un arreglo de NumPy [x', y', z'].
    Raises:
        ValueError: Si el eje proporcionado no es válido.
    '''
    axis = axis.lower()
    if axis == 'x':
        return rot_x(x, y, z, theta)
    elif axis == 'y':
        return rot_y(x, y, z, theta)
    elif axis == 'z':
        return rot_z(x, y, z, theta)
    else:
        raise ValueError("Eje inválido. Debe ser 'x', 'y' o 'z'.")

if __name__ == "__main__":
    # Prueba básica de la función rotar
    punto = (1.0, 0.6, 0.4)
    angulo = np.pi / 2 # 90 grados en radianes
    print("Rotacion alrededor de X:", rotar(*punto, angulo, 'x'))
    print("Rotacion alrededor de Y:", rotar(*punto, angulo, 'y'))
    print("Rotacion alrededor de Z:", rotar(*punto, angulo, 'z'))