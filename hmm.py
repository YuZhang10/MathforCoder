import numpy as np


def forward(A, B, pi, v):
    A_list = [A * B[:, k] for k in range(B.shape[1])]     # 先把A * b算出来，避免重复计算

    alpha = pi * B[:, v[0]]                               # 初始化alpha
    out = [alpha]
    for i in range(1, len(v)):                            # 迭代计算
        alpha = np.dot(A_list[v[i]].T, alpha)
        out.append(alpha)

    result = np.sum(alpha)
    return result, out                                    # 返回最终结果


def backward(A, B, pi, v):
    A_list = [A * B[:, k] for k in range(B.shape[1])]  # 先把A * b算出来，避免重复计算

    beta = np.ones(B.shape[0])
    out = [beta]
    for i in range(len(v) - 1, 0, -1):
        beta = np.dot(A_list[v[i]], beta)
        out.append(beta)

    result = np.sum(np.dot(pi * B[:, v[0]], beta))
    return result, list(reversed(out))


# 传进来的t, i, j默认从1开始
def gamma(alpha, beta, t, i):
    i = i - 1
    alpha, beta = alpha[t-1], beta[t-1]
    partition = np.dot(alpha, beta)
    result = alpha[i] * beta[i] / partition
    return result


def xi(A, B, v, alpha, beta, t, i, j):
    i, j = i - 1, j - 1
    alpha, beta = alpha[t - 1], beta[t] * B[:, v[t]]
    partition = np.dot(np.dot(alpha.T, A), beta)
    result = alpha[i] * A[i, j] * beta[j] / partition
    return result



if __name__ == '__main__':
    A = np.array([[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.3, 0.5]])
    B = np.array([[0.5, 0.5], [0.4, 0.6], [0.7, 0.3]])
    pi = [0.2, 0.4, 0.4]
    v = [0, 1, 0]
    print(forward(A, B, pi, v))
    print(backward(A, B, pi, v))

    _, alpha = forward(A, B, pi, v)
    _, beta = backward(A, B, pi, v)
    print(gamma(alpha, beta, 1, 0))
    print(xi(A, B, v, alpha, beta, 1, 0, 0))

    A = np.array([[0.5, 0.1, 0.4], [0.3, 0.5, 0.2], [0.2, 0.2, 0.6]])
    pi = [0.2, 0.3, 0.5]
    v = [0, 1, 0, 0, 1, 0, 1, 1]
    _, alpha = forward(A, B, pi, v)
    _, beta = backward(A, B, pi, v)
    print(gamma(alpha, beta, 4, 3))
    print(xi(A, B, v, alpha, beta, 1, 0, 0))