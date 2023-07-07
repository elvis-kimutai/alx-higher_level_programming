#!/usr/bin/python3
""" Defines  function multiplies 2 matrices"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply 2 matrices
    Args:
        m_a: first matrix
        m_b: second matrix
    """
    return np.matmul(m_a, m_b)
